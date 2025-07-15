from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from events.models import Events,Booking,CustomUser
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from datetime import date
from django.contrib.auth.decorators import login_required

# admin functions

def admin_login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_admin:
            login(request,user)
            return redirect('admin_event_list')
        else:
            return render(request,'admin/loginpage.html', {'error': 'Invalid username or password'})
    return render(request,'admin/loginpage.html')

def admin_logout_view(request):
    logout(request)
    return redirect('admin_login_view')


@login_required(login_url='admin_login_view')
def admin_event_list(request):
    events = Events.objects.all()
    return render(request,'admin/event_list.html',{"events":events})

@login_required(login_url='admin_login_view')
def add_event(request):
    return render(request,'admin/add_event.html')

@csrf_protect
@login_required(login_url='admin_login_view')
def add_event_post(request):
    if request.method == "POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        datetime_value=request.POST.get('date_time')
        venue=request.POST.get('venue')
        total_seats=request.POST.get('capacity')

        if not (title and description and datetime_value and venue and total_seats):
            messages.error(request,"All fields are required.")
            return render(request,"admin/event_list.html")
        
        try:
            dt_obj = datetime.strptime(datetime_value, "%Y-%m-%dT%H:%M")
            date=dt_obj.date()
            time=dt_obj.time()
        except ValueError:
            messages.error(request, "Invalid date and time format.")
            return render(request,"admin/event_list.html")

        try:
            total_seats = int(total_seats)
        except ValueError:
            messages.error(request,"Capacity must be a number.")
            return render(request,"admin/event_list.html")
        
        Events.objects.create(
            title=title,
            description=description,
            date=date,
            time=time,
            venue=venue,
            total_seats=total_seats
        )
        # return redirect("admin_event_list")
        return HttpResponse("<script>alert('Event Added Successfully.');window.location='/admin_event_list'</script>")
    return render(request,"admin/event_list.html")

@login_required(login_url='admin_login_view')
def delete_event(request,id):
    event=get_object_or_404(Events,id=id)
    event.delete()
    return HttpResponse("<script>alert('Event Deleted Successfully.');window.location='/admin_event_list'</script>")



@login_required(login_url='admin_login_view')
def update_event(request,id):
    event=Events.objects.get(id=id)
    return render(request,'admin/update_event.html',{"event":event})

@login_required(login_url='admin_login_view')
def update_event_post(request,id):
    event=get_object_or_404(Events,id=id)
    if request.method == "POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        datetime_value=request.POST.get('date_time')
        venue=request.POST.get('venue')
        total_seats=request.POST.get('capacity')

        if not (title and description and venue and total_seats):
            messages.error(request,"All fields are required.")
            return render(request,"admin/update_event.html",{"event":event})
        
        if datetime_value:
            try:
                dt_obj = datetime.strptime(datetime_value, "%Y-%m-%dT%H:%M")
                event.date = dt_obj.date()
                event.time = dt_obj.time()
            except ValueError:
                messages.error(request, "Invalid date/time format.")
                return render(request, "admin/update_event.html", {'event': event})

        try:
            event.total_seats = int(total_seats)
        except ValueError:
            messages.error(request, "Capacity must be a number.")
            return render(request, "admin/update_event.html", {'event': event})

        event.title = title
        event.description = description
        event.venue = venue
        event.save()
        return HttpResponse("<script>alert('Event Updated Successfully.');window.location='/admin_event_list'</script>")
    return render(request, "admin/update_event.html", {'event': event})

@login_required(login_url='admin_login_view')
def view_bookings(request,id):
    event_obj=Events.objects.get(id=id)
    bookings=Booking.objects.filter(event=event_obj)
    context={"event":event_obj,"bookings":bookings}
    return render(request,'admin/view_bookings.html',context)



# userside functions

def user_event_list(request):
    events = Events.objects.all()
    return render(request,'user/event_list.html',{"events":events})

def user_book_event(request,id):
    event=Events.objects.get(id=id)
    return render(request,'user/book_event.html',{"event":event})

def book_event_post(request,id):
    event_obj=Events.objects.get(id=id)
    name=request.POST.get('name')
    email=request.POST.get('email')
    seats=request.POST.get('seats')

    if not (name and email and seats):
        return HttpResponse("<script>alert('All fields are required');window.history.back();</script>")

    try:
        seats=int(seats)
    except ValueError:
        return HttpResponse("<script>alert('Invalid number of seats.');window.history.back();</script>")
    if seats > event_obj.seats_left():
        return HttpResponse("<script>alert('Not enough seats available.');window.history.back();</script>")
    event_obj.booked_seats+=seats
    event_obj.save()
    Booking.objects.create(event=event_obj,name=name,email=email,seats_booked=seats)
    send_mail(
        subject="Booking Confirmation",
        message=f"Dear {name}, your booking for '{event_obj.title.strip()}' is confirmed for {seats} seats.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=True
    )
    datetime_combined = datetime.combine(event_obj.date, event_obj.time)
    context={"name":name,"email":email,"seats":seats,"date_time": datetime_combined.strftime("%d %b %Y, %I:%M %p"),"venue":event_obj.venue}
    return render(request,'user/booking_success.html',context)

