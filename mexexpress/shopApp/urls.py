from django.urls import path
from shopApp.views import index,about

app_name = 'app'

urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about')
]