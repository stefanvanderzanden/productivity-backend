from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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
        required=False,
        allow_null=True,
    )
    duration = serializers.DurationField(read_only=True)
    user = CustomUserSerializer(read_only=True)
    ticket = TicketSerializer(read_only=True)
    ticket_id = serializers.PrimaryKeyRelatedField(
        queryset=Ticket.objects.all(),
        source="ticket",
        write_only=True,
        required=False,
        allow_null=True,
    )

    class Meta:
        model = TimeRegistration
        fields = "__all__"

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        if not attrs.get("ticket") and not attrs.get("sub_project"):
            raise ValidationError(
                _("Geef of een ticket op of een project voor de tijdregistratie")
            )
        return validated_data
