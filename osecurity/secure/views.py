from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Credentials
from .serializers import credentialsSerializer
from rest_framework.permissions import IsAuthenticated
from bs4 import BeautifulSoup
import httpx


class Sign_in(APIView):
    def post(self,request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({"detail": "Invalid username or password."}, status=status.HTTP_401_UNAUTHORIZED)
        request.session['user_signed_in'] = True
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        return Response({"access_token": access_token}, status=status.HTTP_200_OK)


class add_Credentials(APIView):
    def post(self,request):
        link = request.data.get('link')
        if Credentials.objects.filter(link=link).exists():
            return Response({"detail": "Credentials already exists."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            with httpx.Client() as client:
                response = client.get(request.data.get('url'))
                response.raise_for_status()
        except httpx.RequestError as e:
            return  Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No title found"
        Cred = Credentials(link=link, title=title)
        Cred.save()
        serializer = credentialsSerializer(Credentials)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class get_Credentials(APIView):
    def get(self,request):
        db_data = Credentials.objects.all()
        serializer = credentialsSerializer(db_data, many=True)
        return Response(serializer.data)