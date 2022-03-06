from django.db import models
from django.urls import reverse

# Create your models here.

class ScrapeJob(models.Model):
    ip = models.CharField(max_length = 50)
    port = models.CharField(max_length = 50)
    protocol = models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)
    region = models.CharField(max_length = 50, null = True, blank = True)
    city = models.CharField(max_length = 50, null = True, blank = True)
    anonymity = models.CharField(max_length = 50)
    speed = models.CharField(max_length = 50)
    uptime = models.CharField(max_length = 50, null = True, blank = True)
    response = models.CharField(max_length = 50)
    last_checked = models.CharField(max_length = 50, null = True, blank = True)

    def __str__(self):
        return self.ip

    class Meta:
        db_table = "proxy"

    class Admin:
        pass

    def edit_url(self):
        return reverse("edit-item", kwargs={"pk":self.pk})


    def delete_url(self):
        return reverse("delete-item", kwargs={"pk":self.pk})   