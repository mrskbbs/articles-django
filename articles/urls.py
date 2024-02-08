from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('' , views.frontpage, name = 'frontpage'),
    path('article/', views.article,  name = 'article'),
    path('article/editor/', views.articleEditor, name = 'editor'),
    path('auth/', views.auth, name = 'auth'),
    path('login/', views.log, name = 'login'),
    path('profile/', views.profile,  name = 'profile'),
]