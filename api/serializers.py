from rest_framework import serializers
from users.models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        ordering = ['-created_at']
        verbose_name = 'User'
        verbose_name_plural = 'Users'
