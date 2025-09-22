from rest_framework import serializers
from .models import Workout, Exercise, Set

class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = ["id", "set_number", "reps", "weight"]

class ExerciseSerializer(serializers.ModelSerializer):

    sets = SetSerializer(many=True, read_only=True)

    class Meta:
        model = Exercise
        fields = ["id", "name", "sets"]

class WorkoutSerializer(serializers.ModelSerializer):

    exercises = ExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = Workout
        fields = ["id", "user", "workout_type", "date", "notes", "exercises"]
