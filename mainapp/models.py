'''
    1. Create tables for diffrent types of categories..!
    2. Change Names of fields
    3. Add List of categories..!
'''
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Author(models.Model):
    blog_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=400)
    full_name = models.CharField(max_length=30)
    photoLink = models.CharField(max_length=150)
    email_link = models.EmailField()
    github_link = models.CharField(max_length=150)
    twitter_link = models.CharField(max_length=150)
    fb_link = models.CharField(max_length=150)

    def __str__(self):
        return self.blog_name


class PageContent(models.Model):
    title = models.CharField(max_length=150)
    desc = models.CharField(max_length=200)
    link_name = models.CharField(max_length=150)
    image_link = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Date Published')
    content = models.TextField()
    tags = models.TextField()

    def __str__(self):
        return self.title


class Tags(models.Model):
    name = models.CharField(max_length=20)
    int_name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
