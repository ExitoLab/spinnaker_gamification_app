import json
from django.shortcuts import render
 
from .models import GithubDetails
from .serializers import GithubDetailsSerializer
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
