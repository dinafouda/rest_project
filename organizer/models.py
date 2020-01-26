from __future__ import unicode_literals

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(max_length=31, unique=True, help_text='A Label for url config')


class Startup(models.Model):
    name = models.CharField(max_length=31, db_index=True)
    slug = models.SlugField(max_length=31, unique=True, help_text='A Label for url config')
    description = models.TextField()
    founded_date = models.DateField("date founded")
    contact = models.EmailField()
    website = models.URLField(max_length=255)
    tags = models.ManyToManyField(Tag)


class NewsLinks(models.Model):
    title = models.CharField(max_length=31)
    slug = models.SlugField(max_length=31)
    pub_date = models.DateField("date published")
    link = models.URLField(max_length=255)
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE())
