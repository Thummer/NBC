from django.urls import path
from core import views
urlpatterns = [
    path('result/', views.result),
    path('input/', views.showInput),
    path('', views.index)
]