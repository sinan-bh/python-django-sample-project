from django.shortcuts import render, HttpResponse
# Create your views here.

def index(req):
    return render(req, 'index.html')

def about(req):
    return render(req, 'about.html')

def booking(req):
    return render(req, 'booking.html')

def doctors(req):
    return render(req, 'doctors.html')

def department(req):
    return render(req, 'department.html')

def contact(req):
    return render(req, 'contact.html')

