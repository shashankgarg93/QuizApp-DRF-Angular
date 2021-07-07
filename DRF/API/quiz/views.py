
# Create your views here.
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from .models import Question
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .serializers import QuestionSerializer
@api_view(['GET','POST'])
def questions(request):
    if(request.method=="GET"):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions,many=True)
        return JsonResponse(serializer.data,safe=False)