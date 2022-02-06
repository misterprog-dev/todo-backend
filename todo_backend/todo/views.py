from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Todo, TodoList
from .serializers import TodoSerializer, TodoListSerializer

class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer
    filterset_fields = ['title', 'completed', 'favorite']
    queryset = Todo.objects.all()

class TodoListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()

