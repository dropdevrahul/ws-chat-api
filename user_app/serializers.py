from rest_framework import serializers
from user_app.models import ApiUser

class LoggedInUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApiUser
        fields = ('id', 'username')
