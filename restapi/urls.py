from django.conf.urls import url 
from restapi import views 
 
urlpatterns = [ 
    url(r'^api/restapi$', views.DjangoGetPostDelete.as_view()),
    url(r'^api/restapi/(?P<pk>[0-9]+)$', views.DjangoGetByIdPutDelete.as_view()),
    url(r'^api/restapi/published$', views.DjangoGetAll.as_view())
]