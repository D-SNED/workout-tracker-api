from rest_framework import viewsets
from .models import Workout, ExerciseLog, SetLog
from .serializers import WorkoutSerializer, ExerciseLogSerializer, SetLogSerializer



class WorkoutViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExerciseLogViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseLogSerializer

    def get_queryset(self):
        return ExerciseLog.objects.filter(workout__user=self.request.user)

class SetLogViewSet(viewsets.ModelViewSet):
    serializer_class = SetLogSerializer

    def get_queryset(self):
        return SetLog.objects.filter(exercise_log__workout__user=self.request.user)
