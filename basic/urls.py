from django.urls import path
from . import views
app_name="basic"
urlpatterns = [
    path('templates/', views.basic_template, name='basic_template'),
    path('templates/basic_form_show', views.basic_form_show, name='basic_form_show'),
    path('templates/basic_form', views.basic_form, name='basic_form'),
    path('templates/basic_form_show2', views.basic_form_show2, name='basic_form_show2'),
    path('templates/basic_form2', views.basic_form2, name='basic_form2'),
    path('templates/basic_form_show3', views.basic_form_show3, name='basic_form_show3'),
]
