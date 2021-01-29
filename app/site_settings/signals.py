from django.core.cache import cache
from django.db.models.signals import post_save

from site_settings.models import SiteSettings


def invalidate_site_settings_cache(sender, instance, **kwargs):
    cache.clear()


post_save.connect(invalidate_site_settings_cache, sender=SiteSettings)