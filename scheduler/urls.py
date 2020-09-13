from django.conf.urls import url 
from scheduler import views 

from django.urls import include, path
from . import views
 
urlpatterns = [ 
    path('issues/', views.issue_external_api_view, name='issue-external-api-view') 
]