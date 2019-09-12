from rest_framework import serializers
from .models import User, Follows

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = [
			'name',
			'username'
		]
		
class FollowsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Follows
		fields = [
			'owner',
			'following'
		]