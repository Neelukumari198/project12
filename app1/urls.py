from django.urls import path
from . views import *
app_name='app1'
urlpatterns=[
    path('',sheryians,name='sheryians'),
    path('home/',home,name='home'),
    path('Bootcamp/',Bootcamp,name='Bootcamp'),
    path('Courses/',Courses,name='Courses'),
    path('RequestCallback/',RequestCallback,name='RequestCallback'),
    path('java/',java,name='java'),
    path('Aptitude/',Aptitude,name='Aptitude'),
    path('backend/',backend,name='backend'),
    path('frontend/',frontend,name='frontend'),

]