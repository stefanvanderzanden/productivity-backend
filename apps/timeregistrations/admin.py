from django.contrib import admin

from apps.timeregistrations.models import TimeRegistration


@admin.register(TimeRegistration)
class TimeRegistrationAdmin(admin.ModelAdmin):
    pass
