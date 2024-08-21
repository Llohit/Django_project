from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import SampleSerializer
from rest_framework import status
import uuid

class Sample(ViewSet):

    serializer_class= SampleSerializer
    def list(self,request):
        return Response("No database to store yet!")
    def create(self,request):
        serializer = self.serializer_class(data= request.data)
        if(serializer.is_valid()):
            data=serializer.validated_data
            print(data)
            unique_uuid=uuid.uuid4()
            data['uid']=unique_uuid
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
