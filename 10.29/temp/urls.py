from django.urls import path
from . import views


urlpatterns = [
    path('article_list/', views.article_list),
    path('article/<article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('article/<article_pk>/comments/', views.comment_create),
]
