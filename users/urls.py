from django.urls import path
from .views import *

urlpatterns = [
    path('/users/current_user', get_current_user),
    path('/users/create', CreateUserView.as_view()),
]
