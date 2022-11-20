from django.db import models

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    About = models.CharField(max_length=200)
    type = models.CharField(max_length=100,choices=(('IT','IT'),
                                                 ('Non-IT','Non_IT'),
                                                 ('Mobile Phone','Mobile Phone')
                                                 ))
    add_date = models.DateTimeField(auto_now=True)
    active= models.BooleanField(default=True)
