from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from restapi.models import Api
from restapi.serializers import ApiSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def api_list(request):
    # GET list of apis, POST a new api, DELETE all apis
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def api_detail(request, pk):
    # find api by pk (id)
    try: 
        api = Api.objects.get(pk=pk) 
    except Api.DoesNotExist: 
        return JsonResponse({'message': 'The api does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE api
    
        
@api_view(['GET'])
def api_list_published(request):