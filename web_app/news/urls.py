from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('<int:id>', new_by_id, name='new_by_id'),
    path('about/',about, name='about'),
    path('contact/', contact, name='contact'),
    path('messages/', messages, name='messages'),
    path('add_news/', add_news, name='add_news'),
    path('post_news/', post_news, name='post_news'),
    path('tag/<str:tag>', by_tag, name='by_tag'),
    path('regestration/', regestrationView, name='regestration'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
]