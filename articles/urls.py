from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('' , views.frontpage, name = 'frontpage'),
    path('profile/<str:username>/', views.profile,  name = 'profile'),
    path('article/<str:article_pk>/', views.article,  name = 'article'),
    path('article/editor/', views.articleEditor, name = 'editor'),
    path('signup/', views.sign_up, name = 'signup'),
    path('login/', views.log_in, name = 'login'),
    path('logout/', views.log_out, name = 'logout'),
]