from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from main import settings

urlpatterns = [
    path('', TemplateView.as_view(template_name="shop/index.html")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
