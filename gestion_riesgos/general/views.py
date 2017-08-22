from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.http import *
from django.template import RequestContext
from django.urls import reverse
from django.template import Context
from django.contrib.auth import authenticate, login as auth_login, logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.hashers  import make_password
from django.contrib.auth.models import *
from .models import *

#from general.models import *
#from general.forms import *

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText 

def handler500(request):
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response

def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

def cerrar_sesion(request):
	logout(request)
	return redirect('login')

def cerrar_sesion(request):
	logout(request)
	return redirect('login')


def login(request):

	ctx = {}
	logout(request)
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request, user)
				return HttpResponseRedirect(reverse('menu'))
		else:
			ctx = {
				 'error': True,
				 'username': username,
			}
	return render(request, 'login.html', ctx)	


@login_required()
def menu(request):
	# return render(request, 'menu_principal.html', {})
	return render(request, 'base.html', {})
