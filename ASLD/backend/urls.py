
from django.urls import path
from . import views
from . import Program

urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('questions', views.questions, name='questions'),
    path('examples', views.examples, name='examples'),
    path('examplestwo', views.examplesTwo, name='examplesTwo'),
    path('main', Program.main, name='main'),
]
