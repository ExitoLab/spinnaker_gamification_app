from django.shortcuts import render

import requests,os
from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.decorators import api_view, renderer_classes 
from rest_framework.renderers import JSONRenderer

from requests.auth import HTTPBasicAuth

from .serializers import *
from .models import *
from rest_framework import filters

from rest_framework.pagination import PageNumberPagination

@api_view(['GET'])
@renderer_classes((JSONRenderer,)) 
def issue_external_api_view(request): #Get the request from the rest api
    try:
        url = "https://api.github.com/repos/{}/{}/issues".format("ExitoLab","spinnaker-ms-teams-notification-plugin")
        r = requests.get(url, verify=False, auth=HTTPBasicAuth(os.environ["GITHUB_USER"], os.environ["GITHUB_TOKEN"]))
        result = r.json()
        if "message" in result and "documentation_url" in result:
            if result['message'] == "Bad credentials":
                return Response("Bad credentials supplied to the API",status=status.HTTP_404_NOT_FOUND)  
    except Exception as e:
        raise (e)
        
    #// check the first record
    # first record is in the db
    #insert the record if nothing exist
    #create a flag to cehck if there are results
    
    recent_record_number = int(result[0]['number'])
    
    new_record_found = 1
    no_record_exist = 1
        
    recent_record_number = {'last_issue_number':recent_record_number}
    
    ##Insert records if it does not exist in the database
    if ( new_record_found == 1 or no_record_exist == 1):
        issue_list = []
        issue_user_list = []
        for data in result:
            response_issue = {"title": data["title"], "created_at": data["created_at"], "updated_at":data["updated_at"], "github_number": data["number"], "github_id": data["id"]}
            response_user = { "login":data["user"]["login"], "type": data["user"]["type"], "github_number": data["number"]}
            issue_list.append(response_issue)
            issue_user_list.append(response_user)
    
        def insert_issues_record(issues, issue_user,recent_record_number):
            print(issues)
            
            #Save issues in the database
            try:
                serializer = IssueSerializer(data=issues, many=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
            except Exception as e:
                raise serializers.ValidationError(e)
            
            #Save issue user in the database
            try:
                issue_user_serializer = IssueUserSerializer(data=issue_user, many=True)
                if issue_user_serializer.is_valid(raise_exception=True):
                    issue_user_serializer.save()
            except Exception as e:
                raise issue_user_serializer.ValidationError(e)
                       
            response = {"status": "Recorded inserted successfully", "message": "The records has been inserted successfully"}
            
            return (response)
    
    api_reponse = insert_issues_record(issue_list,issue_user_list,recent_record_number)
    
    return Response(api_reponse,status=status.HTTP_200_OK)


@api_view(['GET'])
#@permission_classes([AllowAny,])
def ListIssueView(request):
    """
    Provides a get method handler.
    """    
    paginator = PageNumberPagination()
    paginator.page_size = 10
    
    queryset = issue.objects.all()
    result_page = paginator.paginate_queryset(queryset, request)
    serializer_class = IssueSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer_class.data)

# Add view for PR API
@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def pr_external_api_view(request): #Get the request from the rest api
    try:
        url = "https://api.github.com/repos/{}/{}/pulls".format("ExitoLab","spinnaker-ms-teams-notification-plugin")
        r = requests.get(url, verify=False, auth=HTTPBasicAuth(os.environ["GITHUB_USER"], os.environ["GITHUB_TOKEN"]))
        result = r.json()
        print(result)

# Add view for Commit API

@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def commit_external_api_view(request): #Get the request from the rest api
    try:
        url = "https://api.github.com/repos/{}/{}/commits".format("ExitoLab","spinnaker-ms-teams-notification-plugin")
        r = requests.get(url, verify=False, auth=HTTPBasicAuth(os.environ["GITHUB_USER"], os.environ["GITHUB_TOKEN"]))
        result = r.json()
        if "message" in result and "documentation_url" in result:
            if result['message'] == "Bad credentials":
                return Response("Bad credentials supplied to the API",status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        raise (e)

    return Response(result,status=status.HTTP_200_OK)
  
# Add view for Comment API

@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def comment_external_api_view(request): #Get the request from the rest api
    try:
        url = "https://api.github.com/repos/{}/{}/issues/comments".format("ExitoLab","spinnaker-ms-teams-notification-plugin")
        r = requests.get(url, verify=False, auth=HTTPBasicAuth(os.environ["GITHUB_USER"], os.environ["GITHUB_TOKEN"]))
        result = r.json()
        if "message" in result and "documentation_url" in result:
            if result['message'] == "Bad credentials":
                return Response("Bad credentials supplied to the API",status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        raise (e)

    return Response(result, status=status.HTTP_200_OK)