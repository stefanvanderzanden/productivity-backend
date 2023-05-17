from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class TimeRegistration(models.Model):
    project = models.ForeignKey(
        "projects.Project",
        verbose_name=_("Project"),
        on_delete=models.PROTECT,
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

    class Meta:
        verbose_name = _("Tijdregistratie")
        verbose_name_plural = _("Tijdregistraties")
        ordering = ["start"]

    def __str__(self):
        return f"Tijdregistratie voor {self.project.name}"

    @property
    def duration(self):
        if self.end:
            return self.end - self.start
