from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import SampleSerializer
from rest_framework import status
import uuid

class Sample(ViewSet):
    account_ids = []
    serializer_class= SampleSerializer

    def list(self,request):
        if len(self.account_ids):
            acc_id_st = ""
            for acc_id in self.account_ids:
                acc_id_st += str(acc_id) + ","
            acc_id_st = acc_id_st[:-1]

            return Response(f"Account id's added till now are {acc_id_st}")

        return Response(f"No account id's added till now!")

    def create(self,request):
        serializer = self.serializer_class(data= request.data)
        if(serializer.is_valid()):
            data=serializer.validated_data
            unique_uuid=uuid.uuid4()
            data['uid']=unique_uuid
            account_id=data['account']
            self.account_ids.append(account_id)
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
