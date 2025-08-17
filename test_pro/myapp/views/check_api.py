from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CheckView(APIView):
    local_storage = dict()
    def post(self, request):
        print(request)
        self.local_storage['data'] = request.data['data']
        return Response(status=status.HTTP_201_CREATED)
    def get(self,request):
        data = self.local_storage
        return Response(data,status=status.HTTP_200_OK)
