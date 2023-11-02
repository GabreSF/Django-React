from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from .serializers import UserSerializer


class LoginView(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email', '')
        password = data.get('password', '')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login bem-sucedido'})
        else:
            return JsonResponse({'error': 'Credenciais inválidas'}, status=400)

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        first_name = data.get('firstName', '')
        last_name = data.get('lastName', '')
        email = data.get('email', '')
        password = data.get('password', '')

        if not (first_name and last_name and email and password):
            return JsonResponse({'error': 'Todos os campos são obrigatórios'}, status=400)

        User = get_user_model()
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Este email já está em uso'}, status=400)

        user = User.objects.create_user(username=email, password=password, first_name=first_name, last_name=last_name)

        return JsonResponse({'message': 'Registro bem-sucedido'}, status=201)
