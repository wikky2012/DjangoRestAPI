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
        apis = Api.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            apis = apis.filter(title__icontains=title)
        
        apis_serializer = ApiSerializer(apis, many=True)
        return JsonResponse(apis_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        api_data = JSONParser().parse(request)
        api_serializer = ApiSerializer(data=api_data)
        if api_serializer.is_valid():
            api_serializer.save()
            return JsonResponse(api_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # GET list of apis, POST a new api, DELETE all apis
    
    elif request.method == 'DELETE':
        count = Api.objects.all().delete()
        return JsonResponse({'message': '{} Api were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def api_detail(request, pk):
    # find api by pk (id)
    try: 
        api = Api.objects.get(pk=pk) 
    except Api.DoesNotExist: 
        return JsonResponse({'message': 'The api does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE api
    if request.method == 'GET': 
        api_serializer = ApiSerializer(api) 
        return JsonResponse(api_serializer.data) 

    elif request.method == 'PUT': 
        api_data = JSONParser().parse(request) 
        api_serializer = ApiSerializer(api, data=api_data) 
        if api_serializer.is_valid(): 
            api_serializer.save() 
            return JsonResponse(api_serializer.data) 
        return JsonResponse(api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE': 
        api.delete() 
        return JsonResponse({'message': 'Api was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def api_list_published(request):
     # GET all published apis
    apis = Api.objects.filter(published=True)
        
    if request.method == 'GET': 
        apis_serializer = ApiSerializer(apis, many=True)
        return JsonResponse(apis_serializer.data, safe=False)