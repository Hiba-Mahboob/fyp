from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name="Login"),
    path('home', views.home, name="Home"),
    path('studenthome', views.studentHome, name="StudentHome"),
    path('memberhome', views.memberHome, name="MemberHome"),
    path('signupstudent', views.studentSignupPage, name="StudentSignup"),
    path('signupmember', views.memberSignupPage, name="MemberSignup"),
    path('signupuniversity', views.universitySignupPage, name="UniversitySignup"),
    path('handlestudentsignup', views.handleStudentSignup, name="HandleStudentSignup"),
    path('handlemembersignup', views.handleMemberSignup, name="HandleMemberSignup"),
    path('handleuniversitysignup', views.handleUniversitySignup, name="HandleUniversitySignup"),
    path('handlestudentlogin', views.handleStudentLogin, name="handleStudentLogin"),
    path('handlememberlogin', views.handleMemberLogin, name="handleMemberLogin"),
    path('login', views.handleLogin, name="HandleLogin"),
    path('logout', views.handleLogout, name="HandleLogout"),
    path('studenthome/logout', views.handleStudentLogout, name="HandleStudentLogout"),
    path('memberhome/logout', views.handleMemberLogout, name="HandleMemberLogout"),
    path('studentlogin', views.studentLoginPage, name="StudentLogin"),
    path('memberlogin', views.memberLoginPage, name="MemberLogin"),
    path('addquery', views.addQuery, name="AddQuery"),
    
]
