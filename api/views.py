from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


from api import serializer
from api import permissions
from api import models


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profile"""
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    http_method_names = ['get', 'head', 'patch']


class UserProfileViewSet_Student(viewsets.ModelViewSet):
    """Handle creating and updating profile"""
    serializer_class = serializer.UserProfileSerializer_Student
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    http_method_names = ['post', 'head']


class UserProfileViewSet_Teacher(viewsets.ModelViewSet):
    """Handle creating and updating profile"""
    serializer_class = serializer.UserProfileSerializer_Teacher
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    http_method_names = ['post', 'head']

class UserLoginApiView(ObtainAuthToken):
    """Handle creating ser authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES




class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class =serializer.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnProfile,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile = self.request.user)


