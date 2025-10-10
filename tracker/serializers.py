from rest_framework import serializers
from .models import Workout, Exercise, Set

class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = ["id", "exercise", "set_number", "reps", "weight"]

class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = ["id", "workout", "name"]


class WorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workout
        fields = ["id", "user", "workout_type", "date", "notes"]
