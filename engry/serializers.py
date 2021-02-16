from rest_framework import serializers
from engry.models import engryimg


class userSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = engryimg
        fields = '__all__'
