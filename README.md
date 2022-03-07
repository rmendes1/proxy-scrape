<h2 align="center"> 
	🚧 Proxy Scrape 1.0 🚧
</h2>

<p align="center">
 <img alt="Repository size" src="https://img.shields.io/github/repo-size/rmendes1/proxy-scrape">
	
  
  <a href="https://github.com/rmendes1/proxy-scrape/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/rmendes1/proxy-scrape">
  </a>

  <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">
</p>



# Table of Contents
<p align="left">
 • <a href="#description">Description</a> </br>
 • <a href="#tools">Tools</a> </br>
 • <a href="#steps">Steps</a> </br>
 • <a href="#scraping">Scraping</a> </br>
  • <a href="#cleaning-data">Cleaning Data</a> </br>
 • <a href="#pages">Pages</a> </br>
 • <a href="#deploy">Deploy</a> </br>	
 • <a href="#next-steps">Next Steps</a> </br>
 • <a href="#license">License</a>
</p>


# **Description**
This is a fictional site created for a challenge to integrate Django + Webscraping. The aim is to scrape data from a free
proxy site and create a Django application with it, allowing the user to create, update and delete values.


# **Tools**
![Python](https://img.shields.io/badge/-Python-007396?style=flat-square&logo=python&logoColor=ffffff)
![Django](https://img.shields.io/badge/-Django-013220?style=flat-square&logo=Django&logoColor=ffffff)
![HTML](https://img.shields.io/badge/HTML-FFA500?style=flat-square&logo=html&logoColor=ffffff)
![CSS](https://img.shields.io/badge/-CSS-A81D33?style=flat-square&logo=css&logoColor=ffffff)
![Heroku](https://img.shields.io/badge/-Heroku-800080?style=flat-square&logo=heroku&logoColor=ffffff)

# **Steps**
<ol>
  <li>Accessing site url and scrape data</li>
  <li>Cleaning data</li>
  <li>Save to database</li>
  <li>Create Django Setup</li>
  <li>Create Forms, Models, and Views</li>
  <li>Migrating</li>
  <li>Create HTML</li>
  <li>Deploying to Production</li>
</ol>


# **Scraping**

In the current project, the site http://free-proxy.cz/en/ has been selected to be scraped. This site contains the following data:
- IP Address
- Port
- Protocol	
- Country	
- Region	
- City	
- Anonymity	
- Speed	
- Uptime	
- Response	
- Last checked

Since the data in the site's HTML page is already in a tabular form, it was not needed to set up a whole scraper to do it,
as Pandas can get this job done by itself with <code class="lo lp lq lr ls b">pandas.read_html()</code>. This function uses some scraping libraries such as
BeautifulSoup and Urllib to return a list containing all the tables in a page as DataFrames. You just need to pass the URL of the page.
After the extraction, the data is saved in a data frame and transformed into a SQL table.

This function is set inside Django application in (PATH).

# **Cleaning Data**
Inside the table, the IP Address came as an encoded value, so it was necessary to decode and clean it. The correct strings were extracted from
the values and <code class="lo lp lq lr ls b">base64</code> lib helped to decode them into valid IP addresses.

<p align = "center"> Image 1 - Dirty Data </p>
<p align = "center"> <img src="/imgs/encoded_ip.png" />  </p>

<p align = "center"> Image 2 - Cleaned Data IPs </p>
<p align = "center"> <img src="/imgs/decoded_ip.png" />  </p>


# **Pages**
With the aim of this project being to display the data tables and perform CRUD operations, only 2 pages were needed. An index with the list of items and
a forms to add/update new pieces of information to it.

<p align = "center"> Image 3 - Index Page </p>
<p align = "center"> <img src="/imgs/index_page.png" />  </p>

<p align = "center"> Image 4 - Forms (ADD) </p>
<p align = "center"> <img src="/imgs/forms_page.png" />  </p>

<p align = "center"> Image 5 - Forms (UPDATE) </p>
<p align = "center"> <img src="/imgs/forms_update.png" />  </p>


# **Deploy**
<a href="https://proxy-scrape.herokuapp.com/proxy/">
  <img alt="Made by rmendes1" src="https://img.shields.io/badge/Access%20Page%20-Heroku-%2304D361">
</a> <br>
Heroku Cloud was used to deploy this project, as it requires simple settings and generates a direct web access to the project.


# **Next Steps**

Although the app is already deployed and working fine, some problems occur during development phase.

Whereas relatively easy to set locally, uploading the Database with scraped data became more difficult in Heroku's PostgreSQL. 
That is because I had been using SQLAlchemy to create the engine connection and insert the rows there. I still couldn't find a way to update them, so the
Database in production is clean and contains only new info.

Some methods that I think might work:
- Create a local PSQL database and connect with Heroku's PSQL to upload the data;
- Generate via code the command to retrieve Heroku's Postgres URL, which is one of the environment variables set. I tried to use <code class="lo lp lq lr ls b">subprocess</code>
and decode to create a SQLAlchemy engine but I coudn't manage to make it work. The code for that can be found <a href = 'https://github.com/rmendes1/proxy-scrape/blob/main/proxy_scrape/management/commands/scrape_commands_production.py'>here</a>.

# **License**

This project is under MIT License.

Done with ❤️ by João Renato Mendes 👋🏽 [Get in touch!](https://www.linkedin.com/in/joaorenatomendes/)
