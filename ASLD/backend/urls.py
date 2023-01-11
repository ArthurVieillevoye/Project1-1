
from django.urls import path
from . import views
from . import Program

urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('questions', views.questions, name='questions'),
    path('main', Program.main, name='main')
]
