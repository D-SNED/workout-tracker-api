from rest_framework import serializers
from .models import Workout, ExerciseLog, SetLog

class SetLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SetLog
        fields = ["id", "exercise_log", "set_number", "reps", "weight"]

class ExerciseLogSerializer(serializers.ModelSerializer):

    sets = SetLogSerializer(many=True, read_only=True)

    class Meta:
        model = ExerciseLog
        fields = ["id", "workout", "exercise_name", "sets"]

class WorkoutSerializer(serializers.ModelSerializer):

    exercises = ExerciseLogSerializer(many=True, read_only=True)

    class Meta:
        model = Workout
        fields = ["id", "user", "workout_type", "date", "notes", "exercises"]
