from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListCreateAPIView
from .form import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
from .serializer import *
from .permissions import *
from rest_framework.permissions import IsAdminUser


class UserModelViewSet(ListAPIView):
    serializer_class = UserSerializers
    queryset = CustomUser.objects.all()


class FirmModelViewSet(ListAPIView):
    serializer_class = FirmSerializers
    queryset = Firm.objects.all()


class FirmListCreateAPIView(ListCreateAPIView):
    serializer_class = FirmSerializers
    queryset = Firm.objects.all()
    permission_classes = [IsAdminUser, ]


class UserUpdate(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializers
    queryset = CustomUser.objects.all()
    permission_classes = [IsOwnerOrReadOnly, ]


class UserListCreateAPIView(CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsNotOwnerOrReadOnly, ]


class FirmUpdate(RetrieveUpdateDestroyAPIView):
    serializer_class = FirmSerializers
    queryset = Firm.objects.all()

