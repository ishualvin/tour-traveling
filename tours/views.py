from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request,'tour/dashboard.html')

def contact(request):
    return render(request,'tour/contact.html')

def about(request):
    return render(request,'tour/about.html')

def services(request):
    return render(request,'tour/services.html')