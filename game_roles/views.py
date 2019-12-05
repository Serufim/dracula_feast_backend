from rest_framework import generics, permissions

from .models import GameRole
from .serializers import GameRoleSerializer


class GameRolesList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = GameRole.objects.all()
    serializer_class = GameRoleSerializer
# Create your views here.
