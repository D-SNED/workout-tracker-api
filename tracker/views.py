from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Workout, Exercise, Set
from .serializers import WorkoutSerializer, ExerciseSerializer, SetSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [AllowAny]

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [AllowAny]

class SetViewSet(viewsets.ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer
    permission_classes = [AllowAny]
