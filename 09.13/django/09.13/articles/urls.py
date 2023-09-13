from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('dinner/', views.dinner),
    path('search/', views.search),
    path('throw/', views.throw, name="throw"),
    path('catch/', views.catch, name="catch"),
    # path('hello/<str:name>/', views.greeting),
    path('hello/<name>/', views.greeting),
    path('articles/<int:num>/', views.detail),
]