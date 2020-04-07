from django.contrib import admin

from themes.models import Themes


class ThemesAdmin(admin.ModelAdmin):
    model = Themes
    prepopulated_fields = {'slug': ('name',),}


admin.site.register(Themes, ThemesAdmin)