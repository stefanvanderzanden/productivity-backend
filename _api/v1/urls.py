from django.urls import path, include
from rest_framework.routers import SimpleRouter

from apps.projects.views import ProjectViewSet
from apps.snippets.views import SnippetViewSet
from apps.timeregistrations.views import TimeRegistrationViewSet

app_name = "v1"

router = SimpleRouter()
router.register(r"time-registrations", TimeRegistrationViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"snippets", SnippetViewSet)

urlpatterns = [path("", include(router.urls))]
