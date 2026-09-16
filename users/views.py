from rest_framework.response import Response
from django.shortcuts import render
from users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class UserCreateView(APIView):
    def post(self, request):
        
        serializer = UserSerializer(data = request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    "message": "User Created Successfully",
                    "data": serializer.data
                },status = status.HTTP_201_CREATED
            )
        return Response(
            {
                "message": "User creation failed",
                "data": serializer.errors
            }, status = status.HTTP_400_BAD_REQUEST
        )
