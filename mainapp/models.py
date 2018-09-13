from django.db import models


class Author(models.Model):
    blog_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=30)
    email_link = models.EmailField()
    github_link = models.CharField(max_length=100)
    twitter_link = models.CharField(max_length=100)
    fb_link = models.CharField(max_length=100)
    
    def __str__(self):
        return self.blog_name

class PageContent(models.Model):
    title = models.CharField(max_length=100)
    link_name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Date Published')
    content = models.TextField()

    def __str__(self):
        return self.title