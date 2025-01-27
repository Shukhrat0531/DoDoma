from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import User1RegistrationSerializer, User1VerificationSerializer,User1LoginSerializer,CategorySerializer, ProductSerializer,PosterSerializer
from .models import *

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
    

class CategoryAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                category = Category.objects.get(pk=pk)
            except Category.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = CategorySerializer(category)
        else:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PosterAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                category = Poster.objects.get(pk=pk)
            except Poster.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = PosterSerializer(category)
        else:
            categories = Poster.objects.all()
            serializer = PosterSerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PosterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            category = Poster.objects.get(pk=pk)
        except Poster.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PosterSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            category = Poster.objects.get(pk=pk)
        except Poster.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                product = Product.objects.get(pk=pk)
            except Product.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        else:
            products = Product.objects.all()
            paginator = LimitOffsetPagination()
            result_page = paginator.paginate_queryset(products, request)
            serializer = ProductSerializer(result_page, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)