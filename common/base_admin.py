from django.utils import timezone

from django.contrib import admin


class BaseModelAdmin(admin.ModelAdmin):
    exclude = (
        "created_by",
        "updated_by",
        "updated_at",
        "created_at"
    )

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
            obj.updated_by = request.user
            obj.created_at = timezone.now()
            obj.updated_at = timezone.now()

        obj.updated_by = request.user
        obj.updated_at = timezone.now()
        super(BaseModelAdmin, self).save_model(request, obj, form, change)
