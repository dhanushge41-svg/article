from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('news/',news,name='news'),
    path('events/',events,name='events'),
    path('about/',about,name='about'),
    path('read/<int:id>',read,name='read'),
    path('newsread/<int:id>',newsread,name='newsread'),
    path('eventsread/<int:id>',eventsread,name='eventsread'),
    path('aboutread/<int:id>',aboutread,name='aboutread')
  
]