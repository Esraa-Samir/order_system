from django.urls import path
from users.views import *

urlpatterns = [
    path('',UserCreateView.as_view({'get':'list', 'post': 'create'}),name='create-user'),
]