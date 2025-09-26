from rest_framework import serializers
from .models import Repository

class RepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = ['id', 'owner', 'name', 'description', 'is_private', 'created_at']
        read_only_fields = ['owner', 'created_at']
