from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class TimeRegistration(models.Model):
    sub_project = models.ForeignKey(
        "projects.SubProject",
        verbose_name=_("Subproject"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    ticket = models.ForeignKey(
        "projects.Ticket",
        verbose_name=_("Ticket"),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Gebruiker"),
        help_text=_("Selecteer de gebruiker"),
        on_delete=models.PROTECT,
    )
    start = models.DateTimeField(
        verbose_name=_("Starttijd"),
        help_text=_("Geef hier de starttijd op"),
        default=timezone.now,
    )
    end = models.DateTimeField(
        verbose_name=_("Eindtijd"),
        help_text=_("Geef hier de eindtijd op"),
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name=_("Omschrijving"), null=True, blank=True
    )
    external_reference = models.CharField(
        verbose_name=_("Externe referentie"),
        help_text=_("Geef hier een externe referentie op indien van toepassing"),
        max_length=50,
        null=True,
        blank=True,
    )
    duration = models.DurationField(verbose_name=_("Duur"), null=True, blank=True)

    class Meta:
        verbose_name = _("Tijdregistratie")
        verbose_name_plural = _("Tijdregistraties")
        ordering = ["start"]

    @property
    def project(self):
        """Get the main project of a `timeregistrations.TimeRegistration`, if there is a `projects.Ticket`, it is
        through the `projects.SubProject` on the `projects.Ticket` else try to get it through the linked
        `projects.SubProject` on the `timeregistrations.TimeRegistration`
        """
        return (
            self.ticket.sub_project.project
            if self.ticket
            else self.sub_project.project
            if self.sub_project
            else None
        )

    @property
    def project_display_name(self):
        return self.project.name if self.project else ""

    def __str__(self):
        return (
            f"Tijdregistratie {self.description} voor {self.project.name}"
            if self.project
            else f"Tijdregistratie {self.description}"
        )

    def save(self, *args, **kwargs):
        """Override of the save method to
        1. set the duration if there is an end set on the `timeregistrations.TimeRegistration`
        2. always set the sub_project based on the linked `projects.Ticket` if there is one
        """
        if self.end:
            self.duration = self.end - self.start
        if self.ticket:
            self.sub_project = self.ticket.sub_project
        super().save(*args, **kwargs)
