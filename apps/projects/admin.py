from django.contrib import admin

from apps.projects.models import Project, Ticket, TicketType, SubProject


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(SubProject)
class SubProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "project")


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass


@admin.register(TicketType)
class TicketTypeAdmin(admin.ModelAdmin):
    pass
