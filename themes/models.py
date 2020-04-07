from django.db import models
from django.utils import timezone
from django.db import models
from django.db.models import F

from common.base_model import BaseModel


class Themes(BaseModel):
    """
    themes details
    """
    slug = models.CharField(
        max_length=255,
        null=False,
        blank=False, unique=True)

    name = models.CharField(
        max_length=255,
        null=False, blank=False)

    discription = models.TextField()
    is_enabled = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Themes"

    def __str__(self):
        """
        string representation of model
        """
        return self.title

