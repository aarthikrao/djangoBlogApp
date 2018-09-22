from django.urls import path

# from . import views
from . import views

app_name = 'mainapp'

urlpatterns = [
    path(r'<title_name>/', views.index, name='index'),
    path(r'author/', views.render_about, name='render_about'),
    path(r'feed/<title_name>/', views.render_with_title, name='render_with_title')
]