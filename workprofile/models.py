from django.utils import timezone
from django.db import models
from django.db.models import F

from taggit.managers import TaggableManager

from common.utilities import get_upload_path
from common.base_model import BaseModel


class WorkProfiles(BaseModel):
    """
    workprofiles details
    """
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False, unique=True)
    slug = models.SlugField(max_length=255, db_index=True, blank=True)
    name = models.CharField(
        max_length=255,
        null=False, blank=False)
    discription = models.TextField()

    preview_image = models.FileField(
        upload_to=(
            lambda instance, file_name: get_upload_path(
                instance,
                file_name, "preview_image"
            )
        )
    )

    project_files = models.FileField(
        upload_to=(
            lambda instance, file_name: get_upload_path(
                instance,
                file_name, "project-files"
            )
        )
    )

    draft = models.BooleanField(default=True)
    published = models.BooleanField(default=False)
    published_at = models.DateTimeField(
        null=True, blank=True)

    view_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)

    tags = TaggableManager()

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

    def preview_image_url(self):
        """
        project file url
        """
        return self.preview_image.storage.url(self.preview_image.name)

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


class WorkProfileImages(models.Model):
    """
    Images for work profile
    """
    work_profile = models.ForeignKey(
        WorkProfiles,
        related_name="workprofiles",
        on_delete=models.CASCADE)
    alt = models.CharField(max_length=100, null=False, blank=False)
    image = models.FileField(
        upload_to=(
            lambda instance, file_name: get_upload_path(
                instance,
                file_name, "images"
            )
        )
    )
    active = models.BooleanField(default=True)
