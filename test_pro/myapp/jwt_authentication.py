from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import test_pro.settings as settings
import jwt
from .models import User

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        query_params = request.query_params.dict()
        if "user_id" not in query_params:
            return None
        if not auth_header:
            raise AuthenticationFailed("Token required!")
        try:
            jwt_token = auth_header.split(" ")[1]
            payload = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired!")
        except jwt.InvalidSignatureError:
            raise AuthenticationFailed("Invalid token signature!")
        except jwt.DecodeError:
            raise AuthenticationFailed("Invalid token!")
        except Exception as e:
            print(e)
            raise AuthenticationFailed("Authentication failed!")

        token_payload_user_id  = payload['user_id']
        requested_user_id = query_params['user_id']
        if int(requested_user_id) != int(token_payload_user_id):
            raise AuthenticationFailed("Invalid token!")
        try:
            user = User.objects.get(user=token_payload_user_id)
        except User.DoesNotExist:
            raise AuthenticationFailed("User not found!")

        print("Check")
        return user,None



