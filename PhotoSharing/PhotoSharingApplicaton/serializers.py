from rest_framework import serializers
from PhotoSharingApplicaton.models import Users


class UserSerializer(serializers.ModelSerializer):
    # pk = serializers.IntegerField(read_only=True)
    # user_id = serializers.CharField(max_length=30)
    # first_name = serializers.CharField(max_length=30)
    # last_name = serializers.CharField(max_length=30)
    # email = serializers.EmailField()
    # fb_user_id = serializers.CharField(max_length=100, blank=True)
    # fb_access_token = serializers.CharField(max_length=100, blank=True)
    # tw_user_id = serializers.CharField(max_length=100, blank=True)
    # tw_access_token = serializers.CharField(max_length=100, blank=True)
    # gp_user_id = serializers.CharField(max_length=100, blank=True)
    # gp_access_token = serializers.CharField(max_length=100, blank=True)
    # updated_at = serializers.DateField()
    # profile_image = serializers.CharField(max_length=500)
    # created_at = serializers.DateField()

    class Meta:
            model = Users
            fields = ('id', 'user_id', 'first_name', 'last_name', 'email', 'fb_user_id', 'fb_access_token', 'tw_user_id',
             'tw_access_token', 'gp_user_id', 'gp_access_token', 'updated_at', 'profile_image', 'created_at')

    # def create(self, validated_data):
    #
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Users.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('user_id', instance.user_id)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.fb_user_id = validated_data.get('fb_user_id', instance.fb_user_id)
    #     instance.fb_access_token = validated_data.get('fb_access_token', instance.fb_access_token)
    #     instance.tw_user_id = validated_data.get('tw_user_id', instance.tw_user_id)
    #     instance.tw_access_token = validated_data.get('tw_access_token', instance.tw_access_token)
    #     instance.gp_user_id = validated_data.get('gp_user_id', instance.gp_user_id)
    #     instance.gp_access_token = validated_data.get('gp_access_token', instance.gp_access_token)
    #     instance.updated_at = validated_data.get('updated_at', instance.updated_at)
    #     instance.profile_image = validated_data.get('profile_image', instance.profile_image)
    #     instance.created_at = validated_data.get('created_at', instance.created_at)
    #
    #     instance.save()
    #     return instance

