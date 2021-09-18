from superadmin.models import DeptUni, QueryHistory
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .decorators import student_required, superadmin_required, member_required, university_required, department_required
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

def universityLoginPage(request):
    return render(request, 'superadmin/university_login.html')

def departmentLoginPage(request):
    return render(request, 'superadmin/department_login.html')

@login_required
@superadmin_required
def home(request):
    return render(request, 'superadmin/home.html')

@login_required
@member_required
def addQuery(request):
    if request.method=='POST':
        data={
            "tag":request.POST['tag'],
            "pattern":request.POST['pattern'],
            "response":request.POST['response'],
        }


        requests.post("http://127.0.0.1:5000/addquery",json=data)
    
    return render(request, 'superadmin/add_query.html')

@login_required
@university_required
def handleDeleteDept(request):
    if request.method=="POST":
        User.objects.get(username=request.POST['delete-id']).delete()
        DeptUni.objects.get(username=request.POST['delete-id']).delete()
        return redirect("UniversityHome")
    else:
        HttpResponse("Something went wrong")

@login_required
@university_required
def handleUpdateDept(request):
    if request.method=="POST":
        deptuni=DeptUni.objects.get(username=request.POST['username'])
        deptuni.name=request.POST['name']
        deptuni.save()
        return redirect("UniversityHome")
    else:
        HttpResponse("Something went wrong")

@login_required
@university_required
def UpdateDept(request):
    if request.method=="POST":
        return render(request, "UpdateDept")
    else:
        HttpResponse("Something went wrong")

@login_required
@student_required
def studentHome(request):
    queryHistory=QueryHistory.objects.filter(queried_by=request.user)
    context={'response':'','queries':queryHistory}
    if request.method == 'POST':
        query=request.POST.get('query','')
        response = requests.get('https://chatbotuitbackend.herokuapp.com/chatbotquery/'+query)
        responseJSON = response.json()
        context={'response':responseJSON['res'],'query':query}
        QueryHistory.objects.create(query=query, response=responseJSON['res'], queried_by=request.user)
        return render(request, 'superadmin/student_home.html', context)
        # if responseJSON['status']==True:
        #     queryHistory=QueryHistory(query=responseJSON['res'], status=responseJSON['status'])
        #     queryHistory.save()
    return render(request, 'superadmin/student_home.html', context)

@login_required
@member_required
def memberHome(request):
    return render(request, 'superadmin/member_home.html')

@login_required
@university_required
def universityHome(request):
    deptuni=DeptUni.objects.filter(uni=request.user)
    dept_count=DeptUni.objects.filter(uni=request.user).count()
    context={'dept':deptuni,'dept_count':dept_count}
    return render(request, 'superadmin/university_home.html', context)

@login_required
@department_required
def departmentHome(request):
    return render(request, 'superadmin/department_home.html')

@login_required
@university_required
def updateDept(request):
    if request.method == 'POST':
        deptuni=DeptUni.objects.get(username=request.POST['username'])
        context={'deptuni':deptuni}
        return render(request, 'superadmin/update_department.html', context)


@login_required
@university_required
def studentSignupPage(request):
    return render(request, 'superadmin/signup_student.html')

@login_required
@department_required
def memberSignupPage(request):
    return render(request, 'superadmin/signup_member.html')
    
@login_required
@university_required
def departmentSignupPage(request):
    return render(request, 'superadmin/signup_department.html')

@login_required
@superadmin_required
def universitySignupPage(request):
    return render(request, 'superadmin/signup_university.html')

def handleLogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']        
        loginpass=request.POST['loginpass']

        user=authenticate(username=loginusername, password=loginpass)
        print(user)
        if user is not None and user.is_super_admin:
            login(request, user)
            messages.success(request, 'Super admin successfully logged in')
            return redirect('Home')

        else:
            messages.error(request, 'Invalid credentials')
            return redirect('Login')     

    return HttpResponse('404 - Not Found')

@login_required
@university_required
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
@department_required
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

@login_required
@superadmin_required
def handleUniversitySignup(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        user = User.objects.create_user(username=username, password=pass1)
        user.is_university= True
        user.save()

        messages.success(request, "University account has been created successfully")
        return redirect('UniversitySignup')

    else:
        return HttpResponse("404 - Not found")

@login_required
@university_required
def handleDepartmentSignup(request):
    if request.method=="POST":
        username=request.POST['username']
        department=request.POST['department']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        user = User.objects.create_user(username=username, password=pass1)
        user.is_department= True
        user.save()
        DeptUni.objects.create(uni=request.user, name=department, username=username)
        
        messages.success(request, "Department account has been created successfully")
        return redirect('DepartmentSignup')

    else:
        return HttpResponse("404 - Not found")

def handleStudentLogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']        
        loginpass=request.POST['loginpass']

        user=authenticate(username=loginusername, password=loginpass)
        print(user.is_student)
        if user is not None and user.is_student:
            login(request, user)
            messages.success(request, 'Student successfully logged in')
            return redirect('StudentHome')

        else:
            messages.error(request, 'Invalid credentials')
            return redirect('StudentLogin')     
    else:
        return HttpResponse("404 - Not found")

def handleMemberLogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']        
        loginpass=request.POST['loginpass']

        user=authenticate(username=loginusername, password=loginpass)

        if user is not None and user.is_member:
            login(request, user)
            messages.success(request, 'Student successfully logged in')
            return redirect('MemberHome')

        else:
            login(request, user)
            messages.error(request, 'Invalid credentials')
            return redirect('MemberLogin')     
    else:
        return HttpResponse("404 - Not found")

def handleDepartmentLogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']        
        loginpass=request.POST['loginpass']

        user=authenticate(username=loginusername, password=loginpass)

        if user is not None and user.is_department:
            login(request, user)
            messages.success(request, 'Department successfully logged in')
            return redirect('DepartmentHome')

        else:
            login(request, user)
            messages.error(request, 'Invalid credentials')
            return redirect('UniversityLogin')     
    else:
        return HttpResponse("404 - Not found")

def handleUniversityLogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']        
        loginpass=request.POST['loginpass']

        user=authenticate(username=loginusername, password=loginpass)

        if user is not None and user.is_university:
            login(request, user)
            messages.success(request, 'University successfully logged in')
            return redirect('UniversityHome')

        else:
            messages.error(request, 'Invalid credentials')
            return redirect('UniversityLogin')     
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

def handleUniversityLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('UniversityLogin')

def handleDepartmentLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('DepartmentLogin')

             