from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import BucketForm
from .models import Bucket
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
	return render(request,'bucket/home.html')	

def signupuser(request):
	if request.method == 'GET':
		return render(request,'bucket/signupuser.html',{'form':UserCreationForm()})
	else:
		if request.POST['password1']==request.POST['password2']:
			try:
				user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
				user.save()
				login(request,user)
				return redirect('currentbucket')	 
			except IntegrityError:
				return render(request,'bucket/signupuser.html',{'form':UserCreationForm(), 'error':'That username is already been taken :('})
		else:
			return render(request,'bucket/signupuser.html',{'form':UserCreationForm(), 'error':'Passwords did not match'})
			# Tell the user that the paswwords didnt match 

@login_required
def currentbucket(request):
	items=Bucket.objects.filter(user=request.user,datecompleted__isnull=True).order_by('datetocomplete')
	return render(request,'bucket/currentbucket.html',{'items':items})

@login_required
def completedbucket(request):
	items=Bucket.objects.filter(user=request.user,datecompleted__isnull=False).order_by('-datecompleted')
	return render(request,'bucket/completedbucket.html',{'items':items})	

@login_required
def createbucket(request):
	if request.method == 'GET':
		return render(request,'bucket/createbucket.html',{'form':BucketForm()})
	else:
		try:
			form = BucketForm(request.POST)
			newbucketitem = form.save(commit = False)
			newbucketitem.user = request.user
			newbucketitem.save()
			return redirect('currentbucket')	
		except ValueError:
			return render(request,'bucket/createbucket.html',{'form':BucketForm(),'error':'Bad data passed in !! Please try again.'})

def loginuser(request):
	if request.method == 'GET':
		return render(request,'bucket/loginuser.html',{'form':AuthenticationForm()})
	else:
		user =authenticate(request,username=request.POST['username'],password=request.POST['password'])	
		if user is None:
			return render(request,'bucket/loginuser.html',{'form':AuthenticationForm(),'error':'Username or Password incorrect'})
		else:
			login(request,user)
			return redirect('currentbucket')

def logoutuser(request):
	if request.method == 'POST':
		logout(request)
		return redirect('home')	

@login_required
def viewitem(request, item_pk):
	item = get_object_or_404(Bucket, pk=item_pk, user=request.user)
	if request.method == 'GET':
		form = BucketForm(instance=item)
		return render(request,'bucket/viewitem.html',{'item':item, 'form':form })
	else:
		try:
			form = BucketForm(request.POST,instance=item)
			form.save()
			return redirect('currentbucket')
		except ValueError:
			return render(request,'bucket/viewitem.html',{'item':item, 'form':form , 'error':'Bad data passed in !! Please try again.'})	

@login_required
def completeitem(request, item_pk):
	item = get_object_or_404(Bucket, pk=item_pk, user=request.user)
	if request.method == 'POST':
		item.datecompleted = timezone.now()
		item.save()
		return redirect('currentbucket')	

@login_required
def deleteitem(request, item_pk):
	item = get_object_or_404(Bucket, pk=item_pk, user=request.user)
	if request.method == 'POST':
		item.delete()
		return redirect('currentbucket')				