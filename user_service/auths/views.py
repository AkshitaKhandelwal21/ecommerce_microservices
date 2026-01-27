from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from auths.models import Users
from auths.serializers import UserSerializer
from auths.middleware import UserService
from rest_framework.response import Response

# Create your views here.

class RegisterUserView(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):

    def post(self, request):
        username = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'role': user.roles}, status=200)
        
        return Response(
            {'error': 'Invalid username or password'}, status=401
        )
    
class LogoutView():
    pass


class RegisterAsSellerView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user_id")
        if not user_id:
            return
        user = UserService.register_as_seller(user_id)
        return Response({"roles": user.roles})