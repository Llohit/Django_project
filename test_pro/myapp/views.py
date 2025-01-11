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

        #to serialize the model instance into a format like JSON, no validation happening here
        serializer = self.serializer_class(account_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self,request):
        #passing with data keyword, The serializer is used for deserialization (validating and converting incoming data into a model object)
        #This is required as request has data from external src, which needs to be validated b4 storing in db.
        serializer = self.serializer_class(data= request.data)

        # Validate the data provided by user, it will automatically raise exception if deserialization fails.
        serializer.is_valid(raise_exception=True) #Raise exception and return 400 bad request by DRF

        data=serializer.validated_data
        if 'id' in data:
            return Response({f"Unexpected field id provided!"}, status=status.HTTP_400_BAD_REQUEST)
        unique_uuid=uuid.uuid4()
        data['id']=unique_uuid
        #Store in db
        Account.objects.create(**data)
        return Response(data,status=status.HTTP_201_CREATED)

    def retrieve(self,request,pk):
        try:
            account_uid = uuid.UUID(pk)
        except ValueError:
            raise ValueError("Key is not in UUID format")
        try:
            account_details = Account.objects.get(pk=account_uid)
            #to serialize the model instance into a format like JSON, no validation happening here
            serializer = self.serializer_class(account_details)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk):
        try:
            account_uid = uuid.UUID(pk)
        except ValueError:
            raise ValueError("Key is not in UUID format")
        try:
            account_details = Account.objects.get(pk=account_uid)
            account_details.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Account.DoesNotExist:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def patch(self, request, pk):
        try:
            account_uid = uuid.UUID(pk)
        except ValueError:
            raise ValueError("Key is not in UUID format")
        try:
            account_details = Account.objects.get(pk=account_uid)
            new_data = request.data

            #User might only provide data which is required to modify, hence partial is accepted
            serializer = self.serializer_class(data=new_data, partial=True)

            #Validate the data provided by user, it will automatically raise exception if deserialization fails.
            serializer.is_valid(raise_exception=True)

            print(serializer.validated_data)
            #Update the old record with new recd
            account_details.type = new_data.get("type",account_details.type)
            account_details.description = new_data.get("description",account_details.description)
            account_details.save()
            #to serialize the model instance into a format like JSON, no validation happening here
            serializer = self.serializer_class(account_details)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Account.DoesNotExist:
            return Response(status=status.HTTP_403_FORBIDDEN)

# Create your views here.