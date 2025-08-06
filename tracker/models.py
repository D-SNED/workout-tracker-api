from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Workout (models.Model):

    WORKOUT_TYPES = [
    ("push", "Push"),
    ("pull", "Pull"),
    ("legs", "Legs"),
    ("run", "Run"),
    ("mobility", "Mobility"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_type = models.CharField(max_length=20, choices=WORKOUT_TYPES)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)

class ExerciseLog (models.Model):

    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="exercises")
    exercise_name = models.CharField(max_length=50)


class SetLog (models.Model):

    exercise_log_id = models.ForeignKey(ExerciseLog, on_delete=models.CASCADE)
    set_number = models.IntegerField()
