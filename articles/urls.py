from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('' , views.frontpage, name = 'frontpage'),
    path('article/', views.article,  name = 'article'),
    path('article/edit', views.articleEditor,  name = 'editor'),
    path('profile/', views.profile,  name = 'profile'),
]