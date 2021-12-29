from django.shortcuts import render

#imprting functional modules
import pandas
import csv
import json , io
#importing rest framework views
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import AllowAny 
from rest_framework.generics import CreateAPIView , RetrieveAPIView , DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
#importing serializers
from . import serializers

from . import models

class LoadFile(CreateAPIView):
    serializer_class = serializers.FileSerializer
    permission_classes = [AllowAny,]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        file = serializer.data['csv_file'] 
        df = pandas.read_csv(file)
        form_data= {'name':     [],
                    'type':     [],
                    'options':  [],   
                    'mandatory':[]}

        form_data = df.to_dict('list')
        idx = 0 
        form_name = request.data['form_name']
        form_name = {'name':form_name}
        try:
            name_serializer = serializers.FormNameSerializer(data=form_name)
            if name_serializer.is_valid(raise_exception=True):
                name_serializer.save()
            form_object = models.FormName.objects.filter(name=form_name['name'])
            for idx in range(len(form_data['name'])):
                    json_data = {'name':form_data['name'][idx],
                                'type':form_data['type'][idx],
                                'options':form_data['options'][idx],
                                'mandatory':form_data['mandatory'][idx],
                                'form_name':form_object[0].id}
                    print(json_data)
                    serializer = serializers.FormSerailizer(data=json_data)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save()
            return Response({'message':'Entry Created'},status=status.HTTP_201_CREATED)
        except:
            return Response({'message':"You are provide wrong data to make a entry"})

""" 
    CRUD Views for Form Template
"""
@api_view(['POST'])
@permission_classes([AllowAny])
def create_form_entry(request,pk):
    request.data['form_name']=pk
    serializer = serializers.FormSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data,status=status.HTTP_201_CREATED)

#reading form entry specific
class ReadForm(RetrieveAPIView):
    serializer_class = serializers.FormSerailizer()
    permission_classes = [AllowAny,]
    
#

#deleting form entry with primary key
class DeleteFormEntry(DestroyAPIView):
    serializer_class = serializers.FormNameSerializer()
    permission_classes = [AllowAny,]


        