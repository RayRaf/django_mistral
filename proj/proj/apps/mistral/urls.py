from django.urls import path
from . import views

app_name = 'mistral'

urlpatterns = [
    path('', views.main, name='main'),
    path('download/', views.download_docx, name='download_docx'),
]