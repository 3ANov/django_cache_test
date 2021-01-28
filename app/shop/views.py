from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin

from site_settings.models import SiteSettings


class SiteContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_settings = get_object_or_404(SiteSettings, pk=1)
        context['site_title'] = site_settings.title
        context['site_seo_description'] = site_settings.seo_description
        context['site_contact_email'] = site_settings.contact_email
        context['site_logo_image'] = site_settings.logo_image
        context['site_address'] = site_settings.address
        context['site_telephone_number'] = site_settings.telephone_number
        return context


class IndexTemplateView(TemplateView, SiteContextMixin):
    template_name = 'shop/index.html'
