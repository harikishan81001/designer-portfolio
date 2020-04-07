from django.contrib import admin

from common.base_admin import BaseModelAdmin
from workprofile.models import WorkProfiles
from workprofile.models import WorkProfileImages

class WorkProfileImagesInline(admin.TabularInline):
    model = WorkProfileImages
    extra = 1


class WorkProfilesAdmin(BaseModelAdmin):
    model = WorkProfiles
    prepopulated_fields = {'slug': ('title',),}
    list_display = (
        "slug",
        "title",
        "name",
        "draft",
        "published",
        "view_count",
        "likes_count",
        "tag_list"
    )
    search_fields = ("name", "title",)
    list_filter = ("published", "draft", )

    fieldsets = (
        (None, {
            'fields': (
                "title",
                "name",
                "discription",
                "preview_image",
                "project_files",
                "draft",
                "published",
                'tags',
                "slug",
            )
        }),
    )

    inlines = [WorkProfileImagesInline]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


admin.site.register(WorkProfiles, WorkProfilesAdmin)