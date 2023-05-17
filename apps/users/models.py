from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from apps.users.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("E-mailadres"), unique=True)

    first_name = models.CharField(_("Voornaam"), max_length=150, blank=True)
    last_name = models.CharField(_("Achternaam"), max_length=150, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    projects = models.ManyToManyField(
        "projects.Project",
        verbose_name=_("Projecten"),
        help_text=_("Selecteer hier de gewenste projecten voor deze gebruiker")

    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("Gebruiker")
        verbose_name_plural = _("Gebruikers")

    def __str__(self):
        return self.email
