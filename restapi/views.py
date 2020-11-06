from django.shortcuts import render
from rest_framework.generics import get_object_or_404,ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from restapi.models import Api
from rest_framework.views import APIView
from restapi.serializers import ApiSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response




class DjangoGetPostDelete(ListCreateAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer
    permission_classes = (IsAuthenticated,)

    def api_list(self, request):
        if request.method == 'GET':
            apis = Api.objects.all()
            
            title = request.GET.get('title', None)
            if title is not None:
                apis = apis.filter(title__icontains=title)
            
            apis_serializer = ApiSerializer(apis, many=True)
            return JsonResponse(apis_serializer.data, safe=False)
            

        elif request.method == 'POST':
            api_data = JSONParser().parse(request)
            api_serializer = ApiSerializer(data=api_data)
            if api_serializer.is_valid():
                api_serializer.save()
                return JsonResponse(api_serializer.data, status=status.HTTP_201_CREATED) 
            return JsonResponse(api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        elif request.method == 'DELETE':
            count = Api.objects.all().delete()
            return JsonResponse({'message': '{} Api were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
class DjangoGetByIdPutDelete(RetrieveUpdateDestroyAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer
    permission_classes = (IsAuthenticated,)
    
    def api_detail(self, request, pk):

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

class DjangoGetAll(APIView):
    def api_list_published(self,request):
        # GET all published apis
        apis = Api.objects.filter(published=True)
            
        if request.method == 'GET': 
            apis_serializer = ApiSerializer(apis, many=True)
            return JsonResponse(apis_serializer.data, safe=False)