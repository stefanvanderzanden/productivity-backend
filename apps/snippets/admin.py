from django.contrib import admin

from apps.snippets.models import Snippet


@admin.register(Snippet)
class ProjectAdmin(admin.ModelAdmin):
    pass
