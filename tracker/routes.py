from rest_framework.routers import DefaultRouter
from .views import WorkoutViewSet, ExerciseViewSet, SetViewSet

router = DefaultRouter()
router.register(r'workouts', WorkoutViewSet, basename='workout')
router.register(r'exercises', ExerciseViewSet, basename='exercise')
router.register(r'sets', SetViewSet, basename='set')

urlpatterns = router.urls
