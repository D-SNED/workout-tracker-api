from rest_framework import viewsets
from .models import Workout, ExerciseLog, SetLog
from .serializers import WorkoutSerializer, ExerciseLogSerializer, SetLogSerializer
from rest_framework.response import Response


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

