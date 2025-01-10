from .models import BotUser, Feedback
from rest_framework import serializers

class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = ['user_id', 'name', 'username', 'create_at']
        
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['user_id', 'body', 'create_at']
