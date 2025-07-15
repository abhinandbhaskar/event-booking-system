from events.models import Events,Booking
from datetime import date

def next_event(request):
    next_upcoming = Events.objects.filter(date__gte=date.today()).order_by('date','time').first()
    return {'next_upcoming_event':next_upcoming}

def dashboard_counts(request):
    total_events=Events.objects.count()
    total_bookings = 0
    for booking in Booking.objects.all():
        total_bookings+=booking.seats_booked
    return {
        'total_events':total_events,
        'total_tickets_booked':total_bookings,
    }