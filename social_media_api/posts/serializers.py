from rest_framework import serializers
from .models import Post, Comment, Like

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model=Post
        fields=['id', 'title', 'content', 'author', 'comments', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model=Comment
        fields=['id', 'content', 'author', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author']

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Like
        fields = ['id', 'user']
        read_only_fields = ['id', 'user']