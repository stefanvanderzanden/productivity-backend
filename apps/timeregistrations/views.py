import datetime

from django.db.models import Sum
from rest_framework import status
from rest_framework.decorators import action
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
            user=self.request.user,
        )
        response_serializer = self.serializer_class(registrations, many=True)
        total = registrations.aggregate(total=Sum("duration")).get("total")
        return Response(
            {"time_registrations": response_serializer.data, "total": total},
            status=status.HTTP_200_OK,
        )

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.validated_data["user"] = request.user
        time_registration = TimeRegistration.objects.create(**serializer.validated_data)
        response_serializer = self.serializer_class(instance=time_registration)
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path="dashboard-data")
    def dashboard_data(self, request, *args, **kwargs):
        """Fetch total duration per project
        TODO: make this dynamic, in a way the month can be sent with the request parameters
        """
        totals = (
            TimeRegistration.objects.filter(start__year=2023, start__month=5)
            .values("sub_project__name")
            .order_by("sub_project__name")
            .annotate(total_duration=Sum("duration"))
        )

        return Response(list(totals), status=status.HTTP_200_OK)
