from django.urls import path
from . import views

urlpatterns = [
    path('test/<str:code>/', views.api_test),
    path('save_oil/', views.save_oil),
    path('save_gold/', views.save_gold),
    path('save_stock/', views.save_stock),
    path('send_data/<str:code>/', views.send_data),
]
