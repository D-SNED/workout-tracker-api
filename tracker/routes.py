from rest_framework.routers import DefaultRouter
from .views import WorkoutViewSet, ExerciseLogViewSet, SetLogViewSet

router = DefaultRouter()
router.register(r'workouts', WorkoutViewSet, basename='workout')
router.register(r'exerciselogs', ExerciseLogViewSet, basename='exerciselog')
router.register(r'setlogs', SetLogViewSet, basename='setlog')

urlpatterns = router.urls
