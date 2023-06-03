from django.urls import path, include
from rest_framework.routers import SimpleRouter

from apps.projects.views import ProjectViewSet, TicketViewSet, TicketTypeViewSet, SubProjectViewSet
from apps.snippets.views import SnippetViewSet
from apps.timeregistrations.views import TimeRegistrationViewSet

app_name = "v1"

router = SimpleRouter()
router.register(r"time-registrations", TimeRegistrationViewSet, basename="time-registrations")
router.register(r"projects", ProjectViewSet, basename="projects")
router.register(r"sub-projects", SubProjectViewSet, basename='sub-projects')
router.register(r"snippets", SnippetViewSet, basename="snippets")
router.register(r"tickets", TicketViewSet, basename="tickets")
router.register(r"ticket-types", TicketTypeViewSet, basename="ticket-types")

urlpatterns = [path("", include(router.urls))]
