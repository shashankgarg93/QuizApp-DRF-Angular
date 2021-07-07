from rest_framework import serializers
from .models import custom_user


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = custom_user
        fields = "__all__"