from rest_framework import serializers 
from restapi.models import Api
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Api
        fields = ('id',
                  'title',
                  'description',
                  'published')