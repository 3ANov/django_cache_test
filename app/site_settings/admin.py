from django.contrib import admin

# Register your models here.
from site_settings.models import SiteSettings, SocialLink


class SocialLinkInline(admin.StackedInline):
    model = SocialLink
    extra = 1


class SiteSettingsAdmin(admin.ModelAdmin):
    inlines = [SocialLinkInline]


admin.site.register(SiteSettings, SiteSettingsAdmin)

