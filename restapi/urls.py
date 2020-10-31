from django.conf.urls import url 
from restapi import views 
 
urlpatterns = [ 
    url(r'^api/restapi$', views.api_list),
    url(r'^api/restapi/(?P<pk>[0-9]+)$', views.api_detail),
    url(r'^api/restapi/published$', views.api_list_published)
]