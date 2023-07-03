from rest_framework import serializers
from .models import Thing
class ThingSerializers(serializers.ModelSerializer):
    class Meta:
        model=Thing
        fields=('id','owner','name','desc','created_at')