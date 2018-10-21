from django.urls import path

from . import views

app_name = 'NeuralApp'

urlpatterns = [
        path('', views.upload_file, name='upload_file'),
]
