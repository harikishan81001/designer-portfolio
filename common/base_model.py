from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    """
    base model for all app models
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        User,
        related_name="%(app_label)s_%(class)s_related",
        on_delete=models.SET_NULL,
        null=True, blank=True)

    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True
