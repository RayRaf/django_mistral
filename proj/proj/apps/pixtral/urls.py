from django.urls import path
from . import views

app_name = 'pixtral'

urlpatterns = [
    path('', views.main, name='main'),
    path('analyze_image/', views.analyze_image, name='analyze_image'),
]