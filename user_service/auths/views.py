from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from auths.models import Users
from auths.serializers import UserSerializer
from rest_framework.response import Response

# Create your views here.

class RegisterUserView(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        

class LogoutView():
    pass