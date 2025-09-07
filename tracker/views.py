from rest_framework import viewsets
from .models import Workout, ExerciseLog, SetLog
from .serializers import WorkoutSerializer, ExerciseLogSerializer, SetLogSerializer



class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExerciseLogViewSet(viewsets.ModelViewSet):
    queryset = ExerciseLog.objects.all()
    serializer_class = ExerciseLogSerializer

class SetLogViewSet(viewsets.ModelViewSet):
    queryset = SetLog.objects.all()
    serializer_class = SetLogSerializer
