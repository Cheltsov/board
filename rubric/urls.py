from django.urls import path
from . import views

app_name = "rubric"
urlpatterns = [
    path('<int:rubric_pk>/<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/', views.by_rubric, name='by_rubric'),
    path('<str:page>/', views.other_page, name='other'),
    path('', views.index, name='index'),
]
