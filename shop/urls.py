from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('today-deals/', views.today_deals, name='today-deals'),
    path('privacy/', views.privacy, name='privacy'),
    path('about-us/', views.about, name='about-us'),
    path('contact-us/', views.contact, name='contact-us'),
    path('chat/', views.chat, name='chat'),
    path('blog/', views.blog, name='blog'),
    path('faq/', views.faq, name='faq'),
    path('api/contact/', views.contact_api, name='contact_api'),
] 