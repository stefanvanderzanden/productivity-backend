from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Snippet(BaseModel):
    LANGUAGE_CHOICES = (
        ("html", _("HTML")),
        ("python", _("Python")),
        ("sql", _("SQL"))
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("Naam"),
        help_text=_("Geef de snippet een naam")
    )
    description = models.CharField(
        max_length=250,
        verbose_name=_("Omschrijving"),
        help_text=_("Geef een korte omschrijving voor deze snippet"),
        null=True,
        blank=True
    )
    language = models.CharField(
        max_length=6,
        choices=LANGUAGE_CHOICES,
        verbose_name=_("Taal"),
        help_text=_("Geef hier de taal van de snippet op")
    )
    snippet = models.TextField()
    # tags = models.ManyToManyField(
    #     "tags.Tag"
    # )
