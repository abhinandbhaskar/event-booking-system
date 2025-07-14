from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def admin_login(request):
    return render(request,'admin/login.html')

def admin_event_list(request):
    return render(request,'admin/event_list.html')

def add_event(request):
    return render(request,'admin/add_event.html')

def update_event(request):
    return render(request,'admin/update_event.html')

def view_bookings(request):
    return render(request,'admin/view_bookings.html')

# userside functions

def user_event_list(request):
    return render(request,'user/event_list.html')

def user_book_event(request):
    return render(request,'user/book_event.html')

def user_booking_success(request):
    return render(request,'user/booking_success.html')