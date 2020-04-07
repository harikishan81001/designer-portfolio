from django.db import models


class Leads(models.Model):
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    email = models.CharField(max_length=255)
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

    class Meta:
        verbose_name_plural = "Leads"