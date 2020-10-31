from django.conf.urls import url 
from restapi import views 
 
urlpatterns = [ 
    url(r'^api/restapi$', views.tutorial_list),
    url(r'^api/restapi/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/restapi/published$', views.tutorial_list_published)
]