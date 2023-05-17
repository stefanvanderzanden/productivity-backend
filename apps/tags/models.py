from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Tag(BaseModel):
    name = models.CharField(
        verbose_name=_("Tag naam"),
        unique=True
    )
    slug = models.SlugField(
        verbose_name=_("Tag slug"),
        unique=True
    )

    def __str__(self):
        return self.name
