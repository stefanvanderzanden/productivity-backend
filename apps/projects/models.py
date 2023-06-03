from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import CodeTable, BaseModel


class Project(CodeTable):
    pass


class SubProject(CodeTable):
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name=_("Project"),
        help_text=_("Geef hier het project op waar dit project onder valt")
    )


class TicketType(CodeTable):
    pass


class Ticket(BaseModel):
    sub_project = models.ForeignKey(
        "projects.SubProject",
        on_delete=models.PROTECT,
        verbose_name=_("Project"),
        help_text=_("Geef hier het project op voor het ticket"),
        null=True,
        blank=True
    )
    title = models.CharField(
        max_length=120,
        verbose_name=_("Titel"),
        help_text=_("Geef hier een titel op")
    )
    description = models.TextField(
        verbose_name=_("Omschrijving"),
        help_text=_("Geef hier een omschrijving op"),
        null=True,
        blank=True
    )
    ticket_type = models.ForeignKey(
        "projects.TicketType",
        on_delete=models.PROTECT,
        verbose_name=_("Type ticket"),
        help_text=_("Geef hier het type ticket op")
    )
    story_points = models.IntegerField(
        verbose_name=_("Story points"),
        help_text=_("Geef hier het aantal story points op")
    )
    external_id = models.CharField(
        max_length=20,
        verbose_name=_("Externe ID"),
        help_text=_("Geef hier optioneel een extern ID op")
    )