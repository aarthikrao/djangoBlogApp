from django.shortcuts import render
from django.http import HttpResponse
from .models import PageContent, Tags, Author

header_list = Tags.objects.all()


def article(request, title_name):
    posts = PageContent.objects.filter(link_name=title_name)[0]
    render_objects = {
        "header_list": header_list,
        "posts" : posts
    }
    print (render_objects)
    return render(request, 'post.html', render_objects)


def homepage(request):
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
        "post_list": list_of_posts,
        "authorinfo": Author.objects.filter(blog_name=author_name)[0]
    }
    return render(request, 'about.html',render_objects)


def list_post_by_category(request,category):
    list_of_posts = PageContent.objects.filter(tags__icontains=category)
    render_objects = {
        "header_list": header_list,
        "post_list": list_of_posts
    }
    return render(request, 'index_base.html', render_objects)
    
def contact_page(request):
    # list_of_posts = PageContent.objects.filter(tags__icontains=category)
    render_objects = {
        "header_list": header_list,
        # "post_list": list_of_posts
    }
    return render(request, 'contact.html', render_objects)