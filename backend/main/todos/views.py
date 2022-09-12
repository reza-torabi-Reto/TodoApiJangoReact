from django.shortcuts import render
from rest_framework import generics

from .models import Todo
from .serializers import TodosSerializer
# Create your views here.

class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodosSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodosSerializer
