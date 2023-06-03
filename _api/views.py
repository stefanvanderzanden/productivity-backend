from django.contrib.auth import login, logout
from django.utils.translation import gettext_lazy as _
from rest_framework import status, serializers
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from _api.serializers import ApiLoginSerializer


class ApiLoginView(GenericAPIView):
    serializer_class = ApiLoginSerializer
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=self.request.data,
            context={
                "request": self.request
            })
        try:
            serializer.is_valid(raise_exception=True)
        except PermissionDenied:
            return Response(
                _("Geen geldige gebruiker gevonden"),
                status=status.HTTP_401_UNAUTHORIZED
            )
        except serializers.ValidationError:
            raise

        user = serializer.validated_data["user"]
        login(request, user)
        return Response({"id": user.id, "name": user.first_name}, status=status.HTTP_200_OK)


class ApiLogoutView(GenericAPIView):
    permission_classes = ()
    authentication_classes = ()

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response({}, status=status.HTTP_200_OK)


class GetUserView(APIView):

    def get(self, request, *args, **kwargs):
        user = request.user
        return Response({"id": user.id, "name": user.first_name})