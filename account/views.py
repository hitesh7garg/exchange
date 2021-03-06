from django.shortcuts import render
from django.core.urlresolvers import reverse
# Create your views here.
from django.shortcuts import get_object_or_404,redirect,render
from .models import MyUser
from django.http import HttpResponse
from .forms import LoginForm,SignupForm,EditProfile
from django.views.decorators.http import require_http_methods,require_GET,require_POST
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from exch.forms import *
import base64
import json
from django.db.models import Q

@require_GET
def base(request):
	if request.user.is_authenticated():
		return redirect('main')
	questions=Question.objects.all()
	return render(request,'index.html',{'questions':questions})
@require_GET
@login_required
def editProfilePage(request,id):
	form=EditProfile()
	next_url=request.GET.get('next')
	data={'form':form,'next':next_url}
	return render(request,'edit_profile.html',data)
@require_POST
@login_required
def editProfile(request,id):
	f=EditProfile(request.POST,request.FILES,instance=request.user)
	f.actual_user=request.user
	if f.is_valid():
		f.save()
		return redirect('profile',id=id)
	else:
		form=f
		data={'form':form}
		return render(request,'edit_profile.html',data)
		
@require_GET
def renderLogin(request):
	if request.user.is_authenticated():
		return redirect('main')
	next_url=request.GET.get('next')
	loginform=LoginForm()
	data={'loginform':loginform,'next':next_url}
	return render(request,'account/login.html',data)
@require_GET
def renderSignup(request):
	if request.user.is_authenticated():
		return redirect('main')
	next_url=request.GET.get('next')
	signupform=SignupForm(initial={'phone':'+91'})
	data={'signupform':signupform,'next':next_url}
	return render(request,'account/signup.html',data)

@require_POST
def handleLogin(request):
	if request.user.is_authenticated():
		return redirect('main')
	f=LoginForm(request.POST)
	next_url=request.GET.get('next')
	if f.is_valid():
		user=f.get_user()
		login(request,user)
		if not next_url:
			return redirect('main')
		else :
			return redirect(next_url)
	else:
		loginform=f
		signupform=SignupForm(initial={'phone':'+91'})
		data={'signupform':signupform,'loginform':loginform,'next':next_url}
		return render(request,'account/login.html',data)
@require_POST
def handleSignup(request):
	if request.user.is_authenticated():
		return redirect('main')
	f=SignupForm(request.POST)
	next_url=request.GET.get('next')
	if f.is_valid():
		user=f.save()
		user.is_active=True
		user.save()
		return redirect('rlogin')
	else:
		signupform=f
		loginform=LoginForm()
		data={'signupform':signupform,'loginform':loginform,'next':next_url}
		return render(request,'account/signup.html',data)
@require_GET
@login_required
def profile(request,id):
	userprofile=get_object_or_404(MyUser,id=id)
	questions =userprofile.questions_asked.all();
	form=AnswerUploadForm();
	users = MyUser.objects.filter(~Q(id = request.user.id), is_active = True)
	return render(request,'account/user_profile.html',{'questions':questions,'form':form,'userprofile':userprofile,'users':users})
@require_GET
@login_required
def main(request):
	questions = request.user.questions_asked.all();
	for follower in request.user.followers.all():
		questions.add(follower.questions_asked.all())
	answersbyuser=request.user.answered_by.all()
	for follower in request.user.followers.all():
		answersbyuser.add(follower.answered_by.all())
	form=AnswerUploadForm();
	allqs=Question.objects.all()
	return render(request,'indexwithlogin.html',{'questions':questions,'form':form,'answersbyuser':answersbyuser,'allqs':allqs})
@require_GET
@login_required
def logoutview(request):
	if request.user.is_authenticated():
		logout(request)
		return redirect('base')
@require_GET
@login_required
def follow(request, id):
    followee = get_object_or_404(MyUser, id = id)
    follower = request.user
    response_data = {'result': 0}
    if followee.id != follower.id and followee not in follower.following.all():
        follower.following.add(followee)
        response_data['result'] = 1
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        if (followee.id == follower.id):
            response_data['error']  = 'You cannot follow yourself'
        else:
            response_data['error']  = 'You are already following the user'
        return HttpResponse(json.dumps(response_data), content_type="application/json")

@require_GET
@login_required
def unfollow(request, id):
    followee = get_object_or_404(MyUser, id = id)
    follower = request.user
    response_data = {'result': 0}
    if followee.id != follower.id and followee in follower.following.all():
        follower.following.remove(followee)
        response_data['result'] = 1
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        if (followee.id == follower.id):
            response_data['error']  = 'You cannot unfollow yourself'
        else:
            response_data['error']  = 'You are not following the user'
        return HttpResponse(json.dumps(response_data), content_type="application/json")
