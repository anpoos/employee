from django.views.generic import ListView,DetailView,CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from emp.models import Employee
from emp.forms import EmpForm
import datetime
today_date = datetime.datetime.now().date()


class EmpList(ListView):
	model = Employee
	context_object_name = 'emps'
	template_name = "employee_home"
	queryset = Employee.objects.filter(is_deleted=0)


class EmpEdit(LoginRequiredMixin,UpdateView):
	model = Employee
	extra_context = {'updated_date':'2000-10-10'}
	form_class =EmpForm
	template_name = "emp_edit.html"
	success_url = "/"

	def form_valid(self,form):
		emp = form.save(commit=False)
		emp.updated_date = today_date
		emp.save()
		return HttpResponseRedirect('/')

class EmpCreate(LoginRequiredMixin,CreateView):
	model = Employee
	form_class =EmpForm
	template_name = "emp_edit.html"
	success_url = "/employee"


class EmpDelete(LoginRequiredMixin,DeleteView):
	model = Employee
	template_name = "emp_delete.html"
	success_url = "/"

	def post(self,request,**kwargs):
		Employee.objects.filter(id=kwargs['pk']).update(is_deleted=1)
		return HttpResponseRedirect('/')

class EmpDetail(DetailView):
	model = Employee
	context_object_name = 'emp'
	template_name = "emp_detail.html"