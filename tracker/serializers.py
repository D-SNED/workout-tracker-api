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
        fields = ["id", "name", "workout", "sets"]

    def get_fields(self):
        # print("inside get fields")
        fields = super().get_fields()
        request = self.context.get("request")
        print(help(self))
        # print(self.context)
        if request and request.user.is_authenticated:
            fields["workout"].queryset = Workout.objects.filter(user=request.user)
        return fields



class WorkoutSerializer(serializers.ModelSerializer):

    exercises = ExerciseSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Workout
        fields = ["id", "user", "workout_type", "date", "notes", "exercises"]
