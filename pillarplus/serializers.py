from rest_framework import serializers
from . import models


class FileSerializer(serializers.ModelSerializer):
    form_name = serializers.CharField()
    csv_file = serializers.FileField()
    class Meta:
        model= models.FileLoader
        fields = ('csv_file','form_name' )

class FormNameSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    
    class Meta:
        model = models.FormName
        fields = ('name',)


class FormSerailizer(serializers.ModelSerializer):

    class Meta:
        model = models.GoogleForm
        fields = '__all__'
