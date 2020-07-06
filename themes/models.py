from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models import F

from common.base_model import BaseModel
from themes import app_settings


class Themes(BaseModel):
    """
    themes details
    """
    user = models.ForeignKey(
        User, related_name='user_themes', null=False,
        blank=False, on_delete=models.CASCADE)
    slug = models.CharField(
        max_length=255,
        null=False,
        blank=True, unique=True)

    name = models.CharField(
        max_length=255,
        null=False, blank=False, unique=True,
        choices=app_settings.AVAILABLE_THEMES)

    discription = models.TextField()
    is_enabled = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Themes"
        unique_together = (("name", "user", "is_enabled"), )


    def __str__(self):
        """
        string representation of model
        """
        return self.name

    def get_active_theme(self, user):
        return Themes.objects.get(user=user, is_enabeled=True)

