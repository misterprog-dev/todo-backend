from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer

class UserViewSet(viewsets.ViewSet):   
    def list(self, request):
        # utilisateur = User.objects.get(username=request.user)
        # utilisateur_serialise = UserSerializer(utilisateur).data
        # return Response(utilisateur_serialise)
        pass

    def retrieve(self, request, pk=None):
        users = User.objects.all()
        user = get_object_or_404(users, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)