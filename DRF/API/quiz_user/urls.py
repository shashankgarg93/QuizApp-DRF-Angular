from .views import check_user, register_user, sms
from django.urls import path, include
from .api import SimpleApI

urlpatterns = [
    path('hello/', check_user),
    path('register/student/',register_user),
    path('sms/',sms),

]