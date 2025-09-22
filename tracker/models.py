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

    def __str__(self):
        return f"{self.user.username} - {self.workout_type} on {self.date}"

class Exercise (models.Model):

    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="exercises")
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - Workout: {self.workout.id}"


class Set (models.Model):

    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="sets")
    set_number = models.IntegerField()
    reps = models.IntegerField()
    weight = models.FloatField()

    def __str__(self):
        return f"Set {self.set_number}: {self.reps} reps @ {self.weight}"
