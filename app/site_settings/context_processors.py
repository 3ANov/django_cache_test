from django.shortcuts import get_object_or_404

from site_settings.models import SiteSettings, SocialLink


def load_settings(request):
    site_settings = SiteSettings.load()
    return {'site_settings': site_settings,
            'site_social_link': SocialLink.objects.filter(settings_id=site_settings.id)}
