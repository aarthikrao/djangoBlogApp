from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from .models import PageContent, Tags, Author
# HTTP Error 400

header_list = Tags.objects.all()
MAIN_APP_NAME = "My Blog App"


def bad_request(request):
    list_of_posts = PageContent.objects.all()[:10]
    render_objects = {
        "header_list": header_list,
        "post_list": list_of_posts,
        "MAIN_APP_NAME": MAIN_APP_NAME,
        "error_message": "The content you requested for doent seem to be available. However you can view our other posts !"
    }
    return render(request, 'error.html', render_objects)
