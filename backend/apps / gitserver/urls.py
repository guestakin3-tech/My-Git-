from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RepoViewSet

router = DefaultRouter()
router.register(r"repos", RepoViewSet, basename="repo")

urlpatterns = [
    path('', include(router.urls)),
]
