from django.views.generic import ListView

from site_settings.models import SocialLink


class IndexView(ListView):
    template_name = 'shop/index.html'
    queryset = SocialLink.objects.all().order_by('?')
    context_object_name = 'new_social_list'
