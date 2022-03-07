from django.core.management.base import BaseCommand
import requests
import pandas as pd
from proxy_scrape.models import ScrapeJob
import sqlalchemy 
import base64
import subprocess

class Command(BaseCommand):
    help = "collect jobs"
    # define logic of command
    def handle(self, *args, **options):
        header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
        # collect html
        url = 'http://free-proxy.cz/en/proxylist/country/all/https/ping/all'
        page_url = requests.get(url, headers = header)
        df = pd.read_html(page_url.text)

        df_final = df[1].copy()
        df_final['IP address'] = df_final['IP address'].str.extract('"([^"]*)"')
        df_final = df_final[df_final['Port'] != '(adsbygoogle = window.adsbygoogle || []).push({});']
        df_final['IP address'] = df_final['IP address'].apply(lambda x: base64.b64decode(x).decode('utf-8'))
        df_final.columns = ['ip', 'port', 'protocol', 'country', 'region', 'city', 'anonymity', 'speed', 'uptime', 'response', 'last_checked']

        heroku_app_name = "scrape-proxy"
        raw_db_url = subprocess.run(["heroku", "config:get", "DATABASE_URL", "--app", heroku_app_name], capture_output=True).stdout # capture_output arg is added in Python 3.7
        db_url = raw_db_url.decode("ascii").strip()
        final_db_url = "postgresql+psycopg2://" + db_url.lstrip("postgres://")  # lstrip() is more suitable here than replace() function since we only want to replace postgres at the start!
        conn = sqlalchemy.create_engine(final_db_url)

        df_final.to_sql(ScrapeJob._meta.db_table, con = conn, if_exists = "append", index=False, index_label=None, method=None)