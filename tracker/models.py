from django.db import models

class Workout (models.Model):

    WORKOUT_TYPE = [
    ("push", "Push"),
    ("pull", "Pull"),
    ("legs", "Legs"),
    ("run", "Run"),
    ("mobility", "Mobility"),
    ]

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    workout_type = models.CharField(max_length=20, choices=WORKOUT_TYPE)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)
