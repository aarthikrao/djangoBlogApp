from django.shortcuts import render
from django.http import HttpResponse
from .models import PageContent, Tags

header_list = Tags.objects.all()


def article(request, title_name):
    list_of_posts = PageContent.objects.filter(link_name=title_name)
    # render_objects = {
    #     "header_list": header_list,
    #     "post_list": list_of_posts
    # }
    return HttpResponse(list_of_posts)


def homepage(request, title_name):
    list_of_posts = PageContent.objects.all()
    render_objects = {
        "header_list": header_list,
        "post_list": list_of_posts
    }
    return render(request, 'index_base.html', render_objects)


def about_author(request, author_name):
    list_of_posts = PageContent.objects.all()
    render_objects = {
        "header_list": header_list,
        "post_list": list_of_posts
    }
    return render(request, 'about.html',render_objects)


def list_post_by_category(request,category):
    list_of_posts = PageContent.objects.filter(tags__icontains=category)
    render_objects = {
        "header_list": header_list,
        "post_list": list_of_posts
    }
    return render(request, 'index_base.html', render_objects)
    