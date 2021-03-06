# Generated by Django 2.1.1 on 2018-09-09 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=30)),
                ('email_link', models.EmailField(max_length=254)),
                ('github_link', models.CharField(max_length=100)),
                ('twitter_link', models.CharField(max_length=100)),
                ('fb_link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PageContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link_name', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='Date Published')),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Author')),
            ],
        ),
    ]
