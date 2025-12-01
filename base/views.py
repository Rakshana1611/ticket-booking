from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    flights = Flight.objects.all()
    return render(request,'home.html',{'home':True ,'flights': flights})



def history(request):
    booking = Booking.objects.all()
    return render(request,'history.html',{'home':True,'booking': booking})

def book_now(request,flight_id):
    flight = Flight.objects.get(id=flight_id)
    if request.method == "POST":
        booking=Booking.objects.create(
            flight=flight,
            passenger_name=request.POST['passenger_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            aadhaar=request.POST['aadhaar'],
            age=request.POST['age'],
            seat_class=request.POST['seat_class'],
            seat_number=request.POST['seat_number'],
        )
        return redirect('history')
    return render(request,'book_now.html',{'home':True,'flight': flight})



def login(request):
    return render(request,'login.html',{'home':False})

def register(request):
    return render(request,'register.html',{'home':False})

def support(request):
    return render(request,'support.html',{'home':False})

def about(request):
    return render(request,'about.html',{'home':False})

def delete(request, booking_id):
    booking = Booking.objects.get(id=booking_id) 
    booking.delete()
    return redirect('history') 
    