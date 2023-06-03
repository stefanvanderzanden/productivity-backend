from rest_framework import serializers

from apps.projects.models import SubProject, Ticket
from apps.projects.serializers import TicketSerializer, SubProjectSerializer
from apps.timeregistrations.models import TimeRegistration
from apps.users.serializers import CustomUserSerializer


class TimeRegistrationSerializer(serializers.ModelSerializer):
    start = serializers.DateTimeField(input_formats=["%d-%m-%Y %H:%M"])
    end = serializers.DateTimeField(input_formats=["%d-%m-%Y %H:%M"])
    sub_project = SubProjectSerializer(read_only=True)
    sub_project_id = serializers.PrimaryKeyRelatedField(
        queryset=SubProject.objects.all(),
        source="sub_project",
        write_only=True,
        required=False
    )
    duration = serializers.DurationField(read_only=True)
    user = CustomUserSerializer(read_only=True)
    ticket = TicketSerializer(read_only=True)
    ticket_id = serializers.PrimaryKeyRelatedField(
        queryset=Ticket.objects.all(),
        source="sub_project",
        write_only=True,
        required=False
    )

    class Meta:
        model = TimeRegistration
        fields = "__all__"
