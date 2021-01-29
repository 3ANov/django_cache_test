from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView


@method_decorator(cache_page(5*60, key_prefix="index_page"), name='dispatch')
class IndexTemplateView(TemplateView):
    template_name = 'shop/index.html'

