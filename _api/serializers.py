from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied


class ApiLoginSerializer(serializers.Serializer):
    email = serializers.CharField(write_only=True)
    password = serializers.CharField(
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take email address and password from request
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(
                request=self.context.get("request"),
                username=email,
                password=password
            )
            print("USER: ", user)
            if not user:
                raise PermissionDenied
        else:
            msg = _("Both 'username' and 'password' are required.")
            raise serializers.ValidationError(msg, code="authorization")

        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs["user"] = user
        return attrs

