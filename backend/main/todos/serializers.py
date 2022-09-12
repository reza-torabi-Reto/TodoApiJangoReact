from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import *

class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'body']