from rest_framework import generics

from .models import GameRole
from .serializers import GameRoleSerializer

class GameRolesList(generics.ListCreateAPIView):
    queryset = GameRole.objects.all()
    serializer_class = GameRoleSerializer
# Create your views here.
