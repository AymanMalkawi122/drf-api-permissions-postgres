from django.shortcuts import render
from .models import Task
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import TaskSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import ReadOnly
# Create your views here.


class TaskListView(ListCreateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminUser|ReadOnly]


class TaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminUser|ReadOnly]
