from django.views.generic.base import RedirectView
from django.urls import path, re_path, include
from . import views

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^favicon\.ico$', favicon_view),
    path('markdownx/', include('markdownx.urls')),
    path('today-deals/', views.today_deals, name='today-deals'),
    path('privacy/', views.privacy, name='privacy'),
    path('about-us/', views.about, name='about-us'),
    path('contact-us/', views.contact, name='contact-us'),
    path('chat/', views.chat, name='chat'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('faq/', views.faq, name='faq'),
    path('api/contact/', views.contact_api, name='contact_api'),
    path('terms-condition/', views.terms_condition, name='terms-condition'),
] 