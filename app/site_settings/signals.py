from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender='site_settings.SiteSettings')
def invalidate_site_settings_cache(sender, instance, created, **kwargs):
    cache.clear()
