from django.conf.urls import url 
from scheduler import views 

from django.urls import include, path
from . import views
 
urlpatterns = [     
    path('auth/github/', GitHubLogin.as_view())
]