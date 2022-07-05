from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,'base.html')
def studentlogin(request):
    return render(request,'home/studentlogin.html')
def studentsignup(request):
    return render(request,'home/studentsignup.html')
def recruiterlogin(request):
    return render(request,'home/recruiterlogin.html')
def recruitersignup(request):
    return render(request,'home/recruitersignup.html')
def contactus(request):
    return render(request,'home/contactus.html')
def credits(request):
    return render(request,'home/credits.html')
def forgotpassword(request):
    return render(request,'home/ForgotPassword.html')


