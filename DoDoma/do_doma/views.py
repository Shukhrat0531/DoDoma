from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import User1RegistrationSerializer, User1VerificationSerializer,User1LoginSerializer
from .models import User1

class User1RegistrationView(APIView):
    def post(self, request):
        serializer = User1RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Код отправлен на ваш номер"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class User1VerificationView(APIView):
    def post(self, request):
        serializer = User1VerificationSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "Телефон успешно подтвержден"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class User1LoginView(APIView):
    def post(self, request):
        serializer = User1LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "Авторизация успешна"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)