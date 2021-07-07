from django.urls import path, include
from .api import SimpleApI
import rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('hello/', SimpleApI.as_view() ),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
]