from django.urls import path
from . import views

app_name = "main"
urlpatterns = [

    path('accounts/register/activate/<str:sign>/', views.user_activate, name='register_activate'),
    path('accounts/register/done/', views.RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', views.RegisterUserView.as_view(), name='register'),

    path('accounts/password/change/', views.BBPasswordChangeView.as_view(), name='password_change'),

    path('accounts/profile/delete/', views.DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/profile/change/', views.ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/<int:pk>/', views.profile_bb_detail, name='profile_bb_detail'),
    path('accounts/profile/delete/<int:pk>/', views.profile_bb_delete, name='profile_bb_delete'),
    path('accounts/profile/change/<int:pk>/', views.profile_bb_change, name='profile_bb_change'),
    path('accounts/profile/add/', views.profile_bb_add, name='profile_bb_add'),
    path('accounts/profile/', views.profile, name='profile'),

    path('accounts/logout', views.BBLogoutView.as_view(), name='logout'),
    path('accounts/login/', views.BBLoginView.as_view(), name='login'),

    path('<str:page>/', views.other_page, name='other'),
    path('', views.index, name='index'),
]
