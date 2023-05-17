from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_dt = models.DateTimeField(
        auto_now_add=True
    )
    modified_dt = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class CodeTable(models.Model):
    code = models.CharField(
        primary_key=True,
        max_length=50,
        verbose_name=_("Code"),
        help_text=_("Geef hier een code op")
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("Naam"),
        help_text=_("Geef hier een naam op")
    )
    description = models.TextField(
        verbose_name=_("Omschrijving"),
        help_text=_("Geef hier een omschrijving op"),
        null=True,
        blank=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name} ({self.code})"
