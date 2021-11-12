from django.shortcuts import render, HttpResponse
def main(request):
    
    return render(request,'home/main.html')
def signups(request):
    return render(request,'home/signup Students.html')
def signupr(request):
    return render(request,'home/sign up Recruiters.html')
def contact(request):
    return render(request,'home/contacts.html')
def credits(request):
    return render(request,'home/credits.html')


# Create your views here.
