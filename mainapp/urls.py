from django.urls import path

# from . import views
from . import views

app_name = 'mainapp'

urlpatterns = [
    path(r'article/<title_name>/', views.article, name='article'),
    path(r'author/<author_name>/', views.about_author, name='author'),
    path(r'', views.homepage, name='homepage'),
    path('category/contentadd',views.contact_page,name='category'),
    path('category/<category>',views.list_post_by_category,name='category')
]