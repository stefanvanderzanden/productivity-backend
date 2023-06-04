from rest_framework.viewsets import ModelViewSet

from apps.projects.models import Project, Ticket, TicketType, SubProject
from apps.projects.serializers import (
    ProjectSerializer,
    TicketSerializer,
    TicketTypeSerializer,
    SubProjectSerializer
)


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all().order_by("name")


class SubProjectViewSet(ModelViewSet):
    serializer_class = SubProjectSerializer

    def get_queryset(self):
        return SubProject.objects.all().order_by("name")


class TicketViewSet(ModelViewSet):
    serializer_class = TicketSerializer

    def get_queryset(self):
        return Ticket.objects.all().order_by("external_id", "title")


class TicketTypeViewSet(ModelViewSet):
    serializer_class = TicketTypeSerializer

    def get_queryset(self):
        return TicketType.objects.all().order_by("name")
