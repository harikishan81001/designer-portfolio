from django.utils import timezone
from django.db import models
from django.db.models import F

from common.base_model import BaseModel


class WorkProfiles(BaseModel):
    """
    workprofiles details
    """
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False, unique=True)
    slug = models.SlugField(
        max_length=255,
        db_index=True, editable=False)
    name = models.CharField(
        max_length=255,
        null=False, blank=False)
    discription = models.TextField()
    project_files = models.FileField(
        upload_to="work-profiles/project-files")

    draft = models.BooleanField(default=True)
    published = models.BooleanField(default=False)
    published_at = models.DateTimeField(
        null=True, blank=True)

    view_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "WorkProfiles"

    def __str__(self):
        """
        string representation of model
        """
        return self.title

    def project_files_url(self):
        """
        project file url
        """
        return self.project_files.storage.url(self.project_files.name)

    def publish(self):
        """
        publish workprofiles
        """
        self.draft = False
        self.published = True
        self.published_at = timezone.now()
        self.save(update_fields=["draft", "published", "published_at"])

    def incr_view_count(self):
        """
        increment view_count
        """
        self.view_count = F('view_count') + 1
        self.save(update_fields=["view_count"])

    def incr_likes_count(self):
        """
        increment likes_count
        """
        self.likes_count = F('likes_count') + 1
        self.save(update_fields=["likes_count"])
