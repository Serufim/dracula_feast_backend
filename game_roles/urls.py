from django.urls import path

from .views import GameRolesList

urlpatterns = [
    path('/roles', GameRolesList.as_view())
]
