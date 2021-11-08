# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.HyperlinkedIdentityField(
        many=True, read_only=True, view_name="comment-detail"
    )

    class Meta:
        model = Post
        # fields = ['url', 'title', 'link', 'amount_of_upvotes', 'author_name', 'comments']
        fields = "__all__"


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        # fields = ['author_name', 'content', 'post']
        fields = "__all__"
