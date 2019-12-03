from rest_framework import serializers
from .models import GameRole


class GameRoleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'descriptions', 'rules_description', 'image')
        model = GameRole
