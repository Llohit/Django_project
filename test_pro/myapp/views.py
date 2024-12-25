from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import SampleSerializer
from rest_framework import status
import uuid

class Sample(ViewSet):
    account_details = {}
    serializer_class= SampleSerializer

    def list(self,request):
        if len(self.account_details):
            #GET all the list from db
            account_data = self.account_details.values()
            serializer = self.serializer_class(account_data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(f"No account id's added till now!")

    def create(self,request):
        serializer = self.serializer_class(data= request.data)
        if(serializer.is_valid()):
            data=serializer.validated_data
            if 'id' in data:
                return Response({f"Unexpected field id provided!"}, status=status.HTTP_400_BAD_REQUEST)
            unique_uuid=uuid.uuid4()
            data['id']=unique_uuid
            account_id=data['account']
            #Store in db
            self.account_details[account_id] = data
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk):
        account_id = int(pk)
        if account_id not in self.account_details:
            return Response({f"Details for account id:{account_id} is not found"}, status=status.HTTP_403_FORBIDDEN)
        account_details = self.account_details[account_id]
        serializer = self.serializer_class(account_details)
        return Response(serializer.data,status=status.HTTP_200_OK)

# Create your views here.
