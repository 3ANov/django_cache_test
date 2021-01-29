from django.urls import path
from shop.views import IndexTemplateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='home'),
]
