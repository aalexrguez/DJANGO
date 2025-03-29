from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('form_comment/',views.form_comment,name='form_comment'),
    path('form_contact/',views.form_contact,name='form_contact')
]