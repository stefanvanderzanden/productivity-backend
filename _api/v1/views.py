from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# from apps.timetracking.models import TimeRegistration, TimeTrackProject
# from apps.timetracking.serializers import (
#     TimeRegistrationSerializer,
#     TimeTrackProjectSerializer,
# )
#
#
# class TimeRegistrationViewSet(viewsets.ModelViewSet):
#     serializer_class = TimeRegistrationSerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         return TimeRegistration.objects.filter(user=user)
#
#     @action(detail=False, url_name="project-options", url_path="project-options")
#     def project_options(self, request, *args, **kwargs):
#         projects = TimeTrackProject.objects.all()
#         serializer = TimeTrackProjectSerializer(projects, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
