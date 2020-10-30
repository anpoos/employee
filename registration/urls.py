from django.conf.urls import url
from django.views.generic import TemplateView
from registration import views

urlpatterns = [
	url(r'^$', views.Login, name='Login'),
    url(r'^signup/$', views.SignUp.as_view(template_name="register.html")),
	url(r'^logout/$', views.logout_view, name='Login_out'),
]