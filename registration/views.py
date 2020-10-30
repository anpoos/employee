from django.shortcuts import render_to_response, render
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.template import RequestContext
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponseRedirect,HttpResponse
from registration.models import Registration
from registration.forms import RegForm

# Create your views here.

# class Login(TemplateView):
# 	pass
@csrf_exempt
def Login(request):
	if request.method == 'POST':
		print('>>>>>>>>>>>>>>>>>>>>>')
		print(request,">>>>>>>>>>>>>>>>>>>>>>.........")
		username = request.POST.get('email')
		password = request.POST.get('password')
		user = Registration.objects.get(email = username,)
		print(user.password,"?????????")
		print(user.password)
		print(make_password(password))
		if user: 
			request.session['logged_user'] = user.name
			return HttpResponseRedirect('/')
		else:
			return render_to_response('login.html')
	return render_to_response('login.html')
			

class SignUp(CreateView):
	model = Registration
	form_class =RegForm
	template_name = "register.html"

	def post(self,request,**kwargs):
		form =RegForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.password = make_password(password=user.password)
			user.save()
			return HttpResponseRedirect('/registration')
		else:
			form = RegForm()
			return HttpResponseRedirect('/registration/signup')