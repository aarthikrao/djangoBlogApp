from django.shortcuts import render
from django.http import HttpResponse
from .models import PageContent


def index(request, title_name):
    return HttpResponse(title_name)


def render_with_title(request, title_name):
    header_list = {
        "Entertainment": "entertainment",
        "Tech": "tech",
        "Sports": "sports",
        "Fashion": "fashion",
        "Football": "football",
        "Luxury": "luxury",
        "Coding": "Coding",
        "LifeStyle": "lifestyle",
        "Food": "food",
        "Travel": "travel",
        "Litrature": "litrature"
    }

    list_of_posts = PageContent.objects.all()
    render_objects = {"header_list": header_list,
                      "post_list": list_of_posts
                      }
    return render(request, 'index_base.html', render_objects)


def render_about(request, title_name):
    return render(request, 'about.html')
