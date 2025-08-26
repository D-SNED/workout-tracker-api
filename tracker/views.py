from rest_framework import viewsets
from .models import Workout, ExerciseLog, SetLog
from .serializers import WorkoutSerializer, ExerciseLogSerializer, SetLogSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [AllowAny]


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
