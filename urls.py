from django.views.generic import TemplateView
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='login/home.html')),
    url(r'^$', index),
    url(r'^auth/$', auth_view, name= 'check'),
    url(r'^auth2/$', auth_view2, name= 'check2'),
    url(r'^loggedIn/', include('blogser.urls')),
    url(r'^invalid/$', TemplateView.as_view(template_name='login/invalid.html')),
    url(r'^logout/$', logout),
    url(r'^register/$', register, name= 'register'),
    # url('^loggedIn/$', loggedIn),
]
