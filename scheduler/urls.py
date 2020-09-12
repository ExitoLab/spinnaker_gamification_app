from django.conf.urls import url 
from scheduler import views 

from django.urls import include, path
from . import views
 
urlpatterns = [ 
    path('issues/', views.external_api_view, name='external-api-view') 
]