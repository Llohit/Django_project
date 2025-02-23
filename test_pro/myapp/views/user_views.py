from rest_framework.views import APIView
from myapp.models import User
from rest_framework.response import Response
from rest_framework import status
import random
from ..serializer import UserSerializer
from django.http import JsonResponse

class UserAlreadyExists(Exception):
    def __init__(self, message = "A user already exists with same mail id"):
        self.message = message
        super().__init__(self.message)

class UserView(APIView):
    serializer_class = UserSerializer
    def post(self, request):
        email_id = request.data['email']
        password = request.data['password']

        #Check if usrname exists
        user = User.objects.filter(email=email_id) #when you want to avoid exceptions and just get the first match or None.
        if user:
            return Response("User already exists with same email_id!",status=status.HTTP_403_FORBIDDEN)

        user_id = random.randint(1000, 9999)
        try:
            serialized_data = self.serializer_class(data=request.data)
            serialized_data.is_valid(raise_exception=True)
            data = serialized_data.validated_data
            data['user_id'] = user_id
            User.objects.create(user = user_id,email=email_id, password=password)
            data["password"] = "***"
            return Response(data,status=status.HTTP_201_CREATED)
        except Exception as e:
            print("User creation failed due to some reason",e)
            return Response("User creation failed",status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        users = User.objects.all()
        serializer_data = self.serializer_class(users, many=True)
        data = serializer_data.data
        for user in data:
            user['password'] = "***"
        return Response(serializer_data.data,status=status.HTTP_200_OK)
