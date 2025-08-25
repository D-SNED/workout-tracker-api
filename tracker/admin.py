from django.contrib import admin
from .models import Workout, ExerciseLog, SetLog

admin.site.register(Workout)
admin.site.register(ExerciseLog)
admin.site.register(SetLog)
