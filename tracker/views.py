from rest_framework import viewsets
from .models import Workout, Exercise, Set
from .serializers import WorkoutSerializer, ExerciseSerializer, SetSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Workout.objects.filter(user=user)
        return Workout.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        return Exercise.objects.filter(workout__user=self.request.user)

class SetViewSet(viewsets.ModelViewSet):
    serializer_class = SetSerializer

    def get_queryset(self):
        return Set.objects.filter(exercise__workout__user=self.request.user)
