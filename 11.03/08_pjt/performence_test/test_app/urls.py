from django.urls import path
from . import views

urlpatterns = [
    path('load_csv/', views.load_csv, name='load_csv'),
    path('handle_missing_data/', views.handle_missing_data, name='handle_missing_data'),
    path('find_similar_age/', views.find_similar_age, name='find_similar_age'),
]
