from rest_framework import serializers

from apps.projects.models import Project, Ticket, TicketType, SubProject


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"


class SubProjectSerializer(serializers.ModelSerializer):

    project = ProjectSerializer(read_only=True)

    class Meta:
        model = SubProject
        fields = "__all__"


class TicketTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TicketType
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):

    sub_project_id = serializers.PrimaryKeyRelatedField(
        queryset=SubProject.objects.all(),
        source="sub_project",
        write_only=True
    )
    sub_project = SubProjectSerializer(read_only=True)
    ticket_type_id = serializers.PrimaryKeyRelatedField(
        queryset=TicketType.objects.all(),
        source="ticket_type",
        write_only=True
    )
    ticket_type = TicketTypeSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = "__all__"
