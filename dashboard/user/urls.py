from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name="logout"),
    path('dashboard', profile, name='profile'),
    path('add_user', add_user, name='add_user'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete', delete, name='delete'),
]

