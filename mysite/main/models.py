from django.db import models
from datetime import datetime


class Welcome(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    logo = models.ImageField(upload_to='upload')

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    mini_title = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    description = models.TextField()
    logo = models.ImageField(upload_to='upload')
    instagram = models.CharField(max_length=300)
    facebook = models.CharField(max_length=300)
    twitter = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.CharField(max_length=300)
    description = models.TextField()
    logo = models.ImageField(upload_to='upload')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Contact(models.Model):
    logo = models.ImageField(upload_to='upload')
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    email = models.CharField(max_length=300)

    def __str__(self):
        return self.email


class Feedback(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.name


class Reserve(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    peoples = models.IntegerField()
    phone = models.IntegerField()
    date = models.DateTimeField()
    time = models.TimeField()
    message = models.TextField()

    def __str__(self):
        return self.first_name
