# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import auth
from django.shortcuts import render
from django.http import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models  import User
import random

# Create your views here.
otp = 0
user = ''
def index(request):
	form = UserCreationForm()
	return render(request, 'login/home.html', {'form' : form})


def auth_view(request):
	username = request.POST['username']
	password = request.POST['password']
	try:
		global user
		user = auth.authenticate(username=username, password=password)
		global otp
		otp = random.randint(100000,999999)
		print(otp)
		return render(request, 'login/otp.html')
		# auth.login(request, user)
	except:
		return HttpResponseRedirect('/invalid/')
	# return HttpResponseRedirect('/loggedIn/')

def auth_view2(request):
	getotp = request.POST['otp']
	if int(getotp)==otp:
		auth.login(request, user)
		return HttpResponseRedirect('/loggedIn/')
	else:
		return HttpResponseRedirect('/invalid/')
	

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')


def register(request):
	if request.method=="POST":
		form = UserCreationForm(request.POST)
		if form.is_valid:
			form.save()
			return render(request, 'login/register_success.html', {'name': request.POST['username']})
		else:
			return render(request, 'login/invalidr.html')
	# else:
	# 	form = UserCreationForm()
	# return render(request, 'login/register.html', {'form':form})


# def loggedIn(request):
#     if request.user.is_authenticated():
#         return render(request,'login/login.html',{'fullname':request.user.username})
#     else:
#         return HttpResponseRedirect('/')