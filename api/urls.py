from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.User.as_view(), name='users_api'),
    path('user/<int:id>/', views.UserDetail.as_view(), name='user_api'),
]
