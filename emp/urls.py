from django.conf.urls import url
from django.views.generic import TemplateView
from emp import views

urlpatterns = [
	url(r'^$', views.EmpList.as_view(template_name="employee_home.html")),
    url(r'^employee_edit/(?P<pk>[0-9]+)/$', views.EmpEdit.as_view()),    
    url(r'^employee_create/$', views.EmpCreate.as_view()),
    url(r'^employee_delete/(?P<pk>[0-9]+)/$', views.EmpDelete.as_view()),
    url(r'^employee_detail/(?P<pk>[0-9]+)/$', views.EmpDetail.as_view()),

]