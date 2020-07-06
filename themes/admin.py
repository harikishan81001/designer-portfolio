from django.contrib import admin

from common.base_admin import BaseModelAdmin
from themes.models import Themes


class ThemesAdmin(BaseModelAdmin):
    model = Themes
    prepopulated_fields = {'slug': ('name',),}
    fields = ("name", "discription", "user", "is_enabled", "slug",)


admin.site.register(Themes, ThemesAdmin)