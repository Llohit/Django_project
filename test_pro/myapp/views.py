from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import SampleSerializer
from rest_framework import status
from .models import Account
import uuid

class Sample(ViewSet):
    serializer_class= SampleSerializer

    def list(self,request):
        #GET all the list from db
        account_data = Account.objects.all()
        serializer = self.serializer_class(account_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self,request):
        serializer = self.serializer_class(data= request.data)
        if(serializer.is_valid()):
            data=serializer.validated_data
            if 'id' in data:
                return Response({f"Unexpected field id provided!"}, status=status.HTTP_400_BAD_REQUEST)
            unique_uuid=uuid.uuid4()
            data['id']=unique_uuid
            account_id=data['account']
            print(data,"Hi")
            #Store in db
            Account.objects.create(**data)
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk):
        try:
            account_details = Account.objects.get(pk=pk)
            serializer = self.serializer_class(account_details)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk):
        try:
            account_details = Account.objects.get(pk=pk)
            account_details.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Account.DoesNotExist:
            return Response(status=status.HTTP_403_FORBIDDEN)

# Create your views here.