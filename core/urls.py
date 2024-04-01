from django.urls import path
from . import views

urlpatterns = [
    path('', views.site_content, name='home'),
    path('gallery/', views.gallery_content, name ='gallery'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact_view, name='contact'),
]