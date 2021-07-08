from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import Group
from twilio.rest import Client
from .serializers import UserSerializer, UserSerializer2
from .models import custom_user
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import hashlib
@api_view(['GET','POST'])
def check_user(request):
    if(request.method=="POST"):
        user = request.data
        username = user['username']
        password = user['password']
        hashed_pass = hashlib.md5(password.encode()).hexdigest()
        CustomUser = custom_user.objects.filter(username=username)
        if(CustomUser.count()==0):
            return JsonResponse({"Nohi":"Nohi"})
        if(hashed_pass==CustomUser[0].password):
            return JsonResponse({'message':'Hi'})
        return JsonResponse({"message":"Nohi", "username":username})
        # print(user)
        # print(user['username'])


        #return JsonResponse({},safe=False)

@csrf_exempt
@api_view(['GET','POST'])
def register_user(request):
    if(request.method=="POST"):
        #my_student_group = Group.objects.get_or_create(name='STUDENT')
        serializer = UserSerializer(data=request.data)

        hashed_pass = hashlib.md5(request.data['password'].encode())
        serializer.is_valid(raise_exception=True)
        serializer.save(group='S', password = hashed_pass.hexdigest())
        #my_student_group[0].user_set.add(serializer)
        return JsonResponse({"message":"done"})

@api_view(['POST'])
def sms(request):
        if request.method == 'POST':
            account_sid = 'ACab22abe1bb94d8836ff3abc3d0a31e51'
            auth_token = 'b9d96f3193cdc2bc2679c2aea815969c'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                                        body= f'The services are currently only available in Telangana state.',
                                        from_='+17742373181',
                                        to='+918528608198'
                                    )
            
        return JsonResponse({})
