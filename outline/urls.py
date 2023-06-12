from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index_view, name='index_page'),
    path('course/<str:title>', views.topic_view, name='topic_page'),
    path('search', views.search_view, name='search_page'),
    path('new', views.new_page_view, name='new_page'),
    path('edit/<str:title>', views.edit_page_view, name='edit_page'),
    path('random', views.random_page_view, name='random_page'),
]
