from django.urls import path, include

from _api.views import ApiLoginView, ApiLogoutView, GetUserView

app_name = "api"

urlpatterns = [
    path("login/", ApiLoginView.as_view(), name="login"),
    path("logout/", ApiLogoutView.as_view(), name="logout"),
    path("get-user/", GetUserView.as_view(), name="get_user"),
    path("v1/", include("_api.v1.urls", namespace="v1")),
]
