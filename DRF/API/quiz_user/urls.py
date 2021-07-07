from .views import check_user, register_user, sms
from django.urls import path, include
from .api import SimpleApI
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('hello/', check_user),
    path('register/student/',register_user),
    path('sms/',sms),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
]