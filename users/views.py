from pyclbr import Class

from rest_framework.response import Response
from django.shortcuts import render
from users.models import User
from users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.
class UserCreateView(APIView):
    def post(self, request):

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(
                {"message": "User Created Successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"message": "User creation failed", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class UserDetailsView(APIView):

    def get(self, request, pk=None):
        # ============================
        #    GET ALL USERS
        # ============================
        if pk is None:
            user = User.objects.all()
            serializer = UserSerializer(user, many=True)
            return Response(
                {"message": "User List +Retrive Successfuly", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        # ============================
        #    GET ONE USER
        # ============================
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)

            return Response(
                {"message": "User retrieved successfully", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        except User.DoesNotExist:

            return Response(
                {
                    "message": "User not found",
                    "error": "User with the provided ID does not exist.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )


class UserUpdateView(APIView):

    def put(self, request, pk):

        try:
            # 1. Get user from database
            user = User.objects.get(pk=pk)

        except User.DoesNotExist:

            # 2. User not found
            return Response(
                {
                    "message": "User not found",
                    "error": "User with the provided ID does not exist.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        # 3. Send existing user + new data to serializer
        serializer = UserSerializer(
            user,
            data=request.data,
        )

        # 4. Validate data
        if serializer.is_valid():

            # 5. Update user
            serializer.save()

            return Response(
                {"message": "User updated successfully", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        # 6. Validation failed
        return Response(
            {"message": "User update failed", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def patch(self, request, pk):

        try:
            user = User.objects.get(pk = pk)
            except User.DoesNotExist:
                return Response(
                    {
                        "message": "User not found",
                        "error": "User with the provided ID does not exist.",
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )


class UserDeleteView(APIView):

    def delete(self, request, pk):

        try:

            user = User.objects.get(pk=pk)
            user.delete()

            return Response(
                {"message": "User deleted successfully"}, status=status.HTTP_200_OK
            )

        except User.DoesNotExist:

            return Response(
                {
                    "message": "User Not Found",
                    "error": "User with the provided ID does not exist.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )


