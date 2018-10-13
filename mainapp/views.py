from django.shortcuts import render
from django.http import HttpResponse
from .models import PageContent, Tags, Author
from django.http import Http404

header_list = Tags.objects.all()
MAIN_APP_NAME = "My Blog App"

def article(request, title_name):
    try:
        posts = PageContent.objects.filter(link_name=title_name)[0]
    except:
        raise Http404
    render_objects = {
        "header_list": header_list,
        "posts": posts,
        "MAIN_APP_NAME" : MAIN_APP_NAME
    }
    print(render_objects)
    return render(request, 'post.html', render_objects)


def homepage(request):
    list_of_posts = PageContent.objects.all()
    render_objects = {
        "header_list": header_list,
        "post_list": list_of_posts,
        "MAIN_APP_NAME" : MAIN_APP_NAME
    }
    return render(request, 'index_base.html', render_objects)


def about_author(request, author_name):
    list_of_posts = PageContent.objects.all()[:10]
    render_objects = {
        "header_list": header_list,
        "post_list": list_of_posts,
        "authorinfo": Author.objects.filter(blog_name=author_name)[0],
        "MAIN_APP_NAME" : MAIN_APP_NAME
    }
    return render(request, 'about.html', render_objects)


def list_post_by_category(request, category):
    list_of_posts = PageContent.objects.filter(tags__icontains=category)
    render_objects = {
        "header_list": header_list,
        "post_list": list_of_posts,
        "MAIN_APP_NAME" : MAIN_APP_NAME
    }
    return render(request, 'index_base.html', render_objects)


def contact_page(request):
    # list_of_posts = PageContent.objects.filter(tags__icontains=category)
    render_objects = {
        "header_list": header_list,
        "MAIN_APP_NAME" : MAIN_APP_NAME
        # "post_list": list_of_posts
    }
    return render(request, 'contact.html', render_objects)
