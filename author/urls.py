from django.urls import path
from .views import about_view, contact_view

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about')
]