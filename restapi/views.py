from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from restapi.models import Api
from restapi.serializers import ApiSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def api_list(request):
    if request.method == 'GET':
        tutorials = Api.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = ApiSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = ApiSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
     # GET all published apis