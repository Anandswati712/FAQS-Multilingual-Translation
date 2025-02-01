from django.urls import path
from .views import faq_list, home
from django.views.generic import RedirectView
urlpatterns = [
    path('api/faqs/', faq_list.as_view(), name='faq_list'),
    path('', RedirectView.as_view(url='/api/faqs/')),
    path('', home, name='home'),
]