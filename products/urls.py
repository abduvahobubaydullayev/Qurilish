from django.urls import path
from .views import *
from accounts.views import *

urlpatterns = [
    path('products/', ProductListAPIView.as_view()),
    path('buyProducts/', BuyProductListAPIView.as_view()),
    path('products/<int:pk>/', ProductUpdateAPIView.as_view()),
    path('users/', UserModelViewSet.as_view()),
    path('firms/', FirmModelViewSet.as_view()),
    path('user/<int:pk>/', UserUpdate.as_view()),
    path('firms/<int:pk>/', FirmUpdate.as_view()),
    path('product_add/', ProductCreateAPIView.as_view()),
    path('firm_add/', FirmListCreateAPIView.as_view()),
    path('signup/', UserListCreateAPIView.as_view()),
]

