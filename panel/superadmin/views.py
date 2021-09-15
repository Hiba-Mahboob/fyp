from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .decorators import student_required, superadmin_required, member_required
from django.contrib.auth.decorators import login_required
import requests
from django.contrib.auth import get_user_model
User = get_user_model()


def loginPage(request):
    return render(request, 'superadmin/login.html')
    
def studentLoginPage(request):
    return render(request, 'superadmin/student_login.html')

def memberLoginPage(request):
    return render(request, 'superadmin/member_login.html')

@login_required
@superadmin_required
def home(request):
    return render(request, 'superadmin/home.html')

@login_required
@member_required
def addQuery(request):
    return render(request, 'superadmin/add_query.html')

@login_required
@student_required
def studentHome(request):
    context={'response':''}
    if request.method == 'POST':
        query=request.POST.get('query','')
        response = requests.get('https://chatbotuitbackend.herokuapp.com/chatbotquery/'+query)
        responseJSON = response.json()
        context={'response':responseJSON['res'],'query':query}

        # if responseJSON['status']==True:
        #     queryHistory=QueryHistory(query=responseJSON['res'], status=responseJSON['status'])
        #     queryHistory.save()
    return render(request, 'superadmin/student_home.html', context)

@login_required
@member_required
def memberHome(request):
    return render(request, 'superadmin/member_home.html')


@login_required
@superadmin_required
def studentSignupPage(request):
    return render(request, 'superadmin/signup_student.html')

@login_required
@superadmin_required
def memberSignupPage(request):
    return render(request, 'superadmin/signup_member.html')

def handleLogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']        
        loginpass=request.POST['loginpass']

        user=authenticate(username=loginusername, password=loginpass)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, 'Super admin successfully logged in')
            return redirect('Home')

        else:
            login(request, user)
            messages.error(request, 'Invalid credentials')
            return redirect('Login')     

    return HttpResponse('404 - Not Found')

@login_required
@superadmin_required
def handleStudentSignup(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        user = User.objects.create_user(username=username, password=pass1)
        user.is_student= True
        user.save()

        messages.success(request, "Student account has been created successfully")
        return redirect('StudentSignup')

    else:
        return HttpResponse("404 - Not found")

@login_required
@superadmin_required
def handleMemberSignup(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        user = User.objects.create_user(username=username, password=pass1)
        user.is_member= True
        user.save()

        messages.success(request, "Faculty account has been created successfully")
        return redirect('MemberSignup')

    else:
        return HttpResponse("404 - Not found")

def handleStudentLogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']        
        loginpass=request.POST['loginpass']

        user=authenticate(username=loginusername, password=loginpass)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, 'Student successfully logged in')
            return redirect('StudentHome')

        else:
            login(request, user)
            messages.error(request, 'Invalid credentials')
            return redirect('StudentLogin')     
    else:
        return HttpResponse("404 - Not found")

def handleMemberLogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']        
        loginpass=request.POST['loginpass']

        user=authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, 'Student successfully logged in')
            return redirect('MemberHome')

        else:
            login(request, user)
            messages.error(request, 'Invalid credentials')
            return redirect('MemberLogin')     
    else:
        return HttpResponse("404 - Not found")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('Login')

def handleStudentLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('StudentLogin')

def handleMemberLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('MemberLogin')

             