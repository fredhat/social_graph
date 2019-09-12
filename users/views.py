from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User, Follows
from .serializers import UserSerializer

class UserViewSet(viewsets.ViewSet):
	def list(self, request):
		queryset = User.objects.all()
		serializer = UserSerializer(queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def retrieve(self, request, pk=None):
		queryset = User.objects.all()
		user = get_object_or_404(queryset, pk=pk)
		serializer = UserSerializer(user)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def create(self, request):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
		
	@action(detail=True, methods=['get'])
	def followers(self, request, pk=None):
		queryset = User.objects.all()
		user = get_object_or_404(queryset, pk=pk)
		followers = user.followers()
		serializer = UserSerializer([follower.owner for follower in followers], many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
		
	@action(detail=True, methods=['post'], url_path='follow/(?P<follow_pk>[^/.]+)')
	def follow(self, request, follow_pk, pk=None):
		queryset = User.objects.all()
		user = get_object_or_404(queryset, pk=pk)
		target_user = get_object_or_404(queryset, pk=follow_pk)
		successful = Follows().follow(user, target_user)
		if successful:
			return Response(status=status.HTTP_200_OK)
		return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
		
	@action(detail=True, methods=['post'], url_path='unfollow/(?P<follow_pk>[^/.]+)')
	def unfollow(self, request, follow_pk, pk=None):
		queryset = User.objects.all()
		user = get_object_or_404(queryset, pk=pk)
		target_user = get_object_or_404(queryset, pk=follow_pk)
		if user is target_user:
			return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
		successful = Follows().unfollow(user, target_user)
		if successful > 0:
			return Response(status=status.HTTP_200_OK)
		return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
		