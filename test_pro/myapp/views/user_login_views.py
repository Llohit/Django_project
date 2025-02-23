from rest_framework.views import APIView, Response, status

from test_pro import settings
from ..models import User
from ..serializer import UserSerializer
from django.core.exceptions import ObjectDoesNotExist
import datetime
import jwt

class UserLoginView(APIView):
    serializer_class = UserSerializer
    def post(self,request):
        email_id = request.data['email']
        input_pwd = request.data['password']
        try:
            user = User.objects.get(email=email_id)
        except ObjectDoesNotExist:
            return Response("Invalid email_id!", status=status.HTTP_403_FORBIDDEN)
        serialized_data = self.serializer_class(user)
        data = serialized_data.data
        if data['password'] != input_pwd:
            return Response("Invalid password!", status=status.HTTP_403_FORBIDDEN)
        #User is authenticated, now creating jwt token
        payload = {
            "user_id": data["user"],
            "created_at": datetime.datetime.utcnow().isoformat()
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return Response({"token":token}, status=status.HTTP_200_OK)
