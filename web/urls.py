from django.urls import path, include
from web import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/', views.ajax, name='ajax'),
]