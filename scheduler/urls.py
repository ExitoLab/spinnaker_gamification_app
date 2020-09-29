from django.conf.urls import url 
from scheduler import views 

from django.urls import include, path
from . import views
 
urlpatterns = [ 
    path('issues/', views.issue_external_api_view, name='issue-external-api-view'),
    path('list_issues/', views.ListIssueView, name='list-issue-view'),
    path('pulls/', views.pr_external_api_view, name='pr-external-api-view'),
    path('commits/', views.commit_external_api_view, name='commit-external-api-view'),
    path('comments/', views.comment_external_api_view, name='comment-external-api-view')
]