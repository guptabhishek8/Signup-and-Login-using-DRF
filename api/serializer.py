from rest_framework import serializers

from api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password', 'is_student', 'sap_id', 'dept_name')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }


class UserProfileSerializer_Teacher(serializers.ModelSerializer):
    """Serializes a user  profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password', 'is_student', 'sap_id', 'dept_name')
        extra_kwargs = {
            'is_student': {
                'read_only': True,
                'default': False
            },

            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            },
            'sap_id': {
                'read_only': True,
                'default': 'Null'
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""

        user = models.UserProfile.objects.create_user_teacher(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            dept_name=validated_data['dept_name'],
        )
        return user


class UserProfileSerializer_Student(serializers.ModelSerializer):
    """Serializes a Student user  profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password', 'is_student', 'sap_id', 'dept_name')
        extra_kwargs = {
            'is_student': {
                'read_only': True,
                'default':True
            },

            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            },
            'dept_name': {
                'read_only': True,
                'default': 'Null'
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""

        user = models.UserProfile.objects.create_user_student(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            sap_id=validated_data['sap_id'],
        )
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {
            'user_profile': {'read_only': True},
            'status_text': {'read_only': True}

        }
