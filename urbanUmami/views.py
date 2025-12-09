from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'urbanUmami/about.html')

def home(request):
    return render(request, 'urbanUmami/home.html')

def index(request):
    return render(request, 'urbanUmami/index.html')

def menu(request):
    return render(request, 'urbanUmami/menu.html')

def order(request):
    return render(request, 'urbanUmami/orders.html')

def profile(request):
    return render(request, 'urbanUmami/profile.html')

def reserve(request):
    return render(request, 'urbanUmami/reserve.html')

def contact(request):
    return render(request,'urbanUmami/contact.html')

<<<<<<< HEAD
def chinese(request):
    return render(request,'urbanUmami/chinese.html')

def indian(request):
    return render(request,'urbanUmami/indian.html')

def continental(request):
    return render(request,'urbanUmami/continental.html')
=======
def feedback(request):
    return render(request,'urbanUmami/feedback.html')
>>>>>>> e732168a4c7c98e402982b6b67e00c8d950dbdd8
