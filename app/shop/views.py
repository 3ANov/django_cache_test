from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin
from django.http import HttpResponse
from site_settings.models import SiteSettings, SocialLink
from django.core.cache import cache


@method_decorator(cache_page(5*60, key_prefix="index_page"), name='dispatch')
class IndexTemplateView(TemplateView):
    template_name = 'shop/index.html'


def show_cache_view(request):
    return HttpResponse(cache.get('SiteSettings'))