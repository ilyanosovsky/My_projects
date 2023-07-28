from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name='user-detail', queryset=User.objects.all())
    class Meta:
        model = Post
        fields = ('title', 'category', 'publlish_date', 'last_update', 'author')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)