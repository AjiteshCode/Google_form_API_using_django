from django.db.models import query
from rest_framework import serializers
from . import models


class FileSerializer(serializers.ModelSerializer):
    form_name = serializers.CharField()
    csv_file = serializers.FileField()
    class Meta:
        model= models.FileLoader
        fields = ('csv_file','form_name' )

class FormSerailizer(serializers.ModelSerializer):

    class Meta:
        model = models.GoogleForm
        fields = '__all__'

class FormNameSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    entries = serializers.SerializerMethodField('all_entries',read_only=True)
    class Meta:
        model = models.FormName
        fields = "__all__"
       
    def all_entries(self,obj):
        queryset = models.GoogleForm.objects.filter(form_name=obj.id)
        data={'name':[],'type':[],'options':[],'mandatory':[]}
        for i in queryset:
            data['name'].append(i.name)
            data['type'].append(i.type)
            data['options'].append(i.options)
            data['mandatory'].append(i.mandatory)
        return data


 