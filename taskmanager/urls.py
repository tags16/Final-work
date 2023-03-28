from rest_framework.routers import DefaultRouter
from .views import TodolistViewSet

router = DefaultRouter()
app_name = "taskmanagerapp"

router.register(
    prefix="tasks",
    viewset=TodolistViewSet,
    basename="tasks",
)
urlpatterns = router.urls