from rest_framework import serializers

from apps.projects.models import Project
from apps.projects.serializers import ProjectSerializer
from apps.timeregistrations.models import TimeRegistration
from apps.users.serializers import CustomUserSerializer


class TimeRegistrationSerializer(serializers.ModelSerializer):
    start = serializers.DateTimeField(input_formats=["%d-%m-%Y %H:%M"])
    end = serializers.DateTimeField(input_formats=["%d-%m-%Y %H:%M"])
    project = ProjectSerializer(read_only=True)
    duration = serializers.DurationField(read_only=True)
    project_id = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(),
        source="project",
        write_only=True,
        required=True
    )
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = TimeRegistration
        fields = "__all__"
