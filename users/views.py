from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer


class UserCreateView(viewsets.ModelViewSet):
    """
    Create User (sign up)
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()