from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from main import settings
from shop.views import IndexTemplateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='home'),
]
