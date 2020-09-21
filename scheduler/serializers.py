from rest_framework import serializers

from . import models

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'created_at', 'updated_at', 'github_number', 'github_id', 'date_created_at','date_updated_at')
        model = models.issue

class IssueUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'login','type','github_number','created_at','updated_at',)
        model = models.issue_user
        
class IssueLastNumberSerializer(serializers.ModelSerializer):
      class Meta:
        fields = ('id', 'last_issue_number','created_at','updated_at',)
        model = models.record_last_number

class PullSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'created_at', 'updated_at', 'github_number', 'github_id', 'login', 'state', 'body', 'date_created_at','date_updated_at')
        model = models.pull_request

