import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.core.serializers import DateSerializer
from apps.timeregistrations.models import TimeRegistration
from apps.timeregistrations.serializers import TimeRegistrationSerializer


class TimeRegistrationViewSet(ModelViewSet):
    serializer_class = TimeRegistrationSerializer
    queryset = TimeRegistration.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = DateSerializer(data=self.request.GET)
        serializer.is_valid(raise_exception=True)
        date_filter = serializer.validated_data.get("date")
        registrations = TimeRegistration.objects.filter(
            start__date__gte=date_filter,
            start__date__lte=(date_filter + datetime.timedelta(days=6)),
            user=self.request.user)
        response_serializer = self.serializer_class(registrations, many=True)
        total = sum([registration.duration for registration in registrations], start=datetime.timedelta())
        return Response({
            "time_registrations": response_serializer.data,
            "total": total
        }, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.validated_data["user"] = request.user
        time_registration = TimeRegistration.objects.create(
            **serializer.validated_data
        )
        response_serializer = self.serializer_class(instance=time_registration)
        return Response(response_serializer.data, status=status.HTTP_200_OK)
