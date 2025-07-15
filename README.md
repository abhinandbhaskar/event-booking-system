# EasyEvents - Event & Ticket Booking System

**EasyEvents** is a Django-based mini event booking system built for community centers or small auditoriums.  
It allows visitors to view events, book tickets, and lets admins manage events and bookings through a secure dashboard.

---

## Features

### Visitor Features:
- View a list of upcoming events in **card-style design**
- Each event card displays:  
  **Title, Description, Venue, Date & Time, Seats Left**
- If seats are available:  
  Visitors see a **"Book Now"** button that redirects them to the event’s booking page  
  (where they can see full event details and a booking form with Name, Email, Number of Seats)
- If the event is sold out:  
  Visitors see a **"Sold Out"** label instead of the "Book Now" button
- After booking, a **confirmation page** is displayed with booking details
- A **booking confirmation email** is sent to the console (for testing purposes)

---

### Admin Features:
- Secure admin login system using a **custom user model** (`CustomUser` with `is_admin` flag)
- Access control implemented with **login-required decorators**
- Clean, user-friendly **Admin Dashboard** showing:
  - Total Number of Events
  - Total Tickets Booked
  - Quick Actions: **Add New Event**, **View All Events**, **Logout**
- **Event Management:**
  - Add new events with fields — Title, Short Description, Date & Time, Venue, Capacity
  - Edit existing events
  - Delete events when needed
  - Events automatically marked as **"Sold Out"** when fully booked
- **View Bookings for Each Event:**
  - Detailed booking table showing **Name, Email, Seats Booked, Booking Date & Time**
  - Display of event summary — Title, Description, Venue, Date & Time, Total Seats, Booked Seats, Seats Left
- **Admin Logout** functionality

---

### Extra Features:
- **Custom Template Filter:**  
  Display available seats left for each event dynamically in templates
- **Context Processor:**  
  Inject global data into templates, such as:
  - The next upcoming event (for visitor navbar)
  - Total number of events (for admin dashboard)
  - Total tickets booked (for admin dashboard)
- **Console Email Backend:**  
  Simulate booking confirmation emails using Django's console backend (for testing)

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/abhinandbhaskar/event-booking-system.git
   cd event-booking-system


2. **Create & Activate Virtual Environment:**
python -m venv venv
venv\Scripts\activate    # For Windows
# source venv/bin/activate    # For macOS/Linux


3. **Install Dependencies:**
pip install -r requirements.txt


4.**Apply Migrations:**
python manage.py makemigrations
python manage.py migrate


5. **Create Admin User:**
python manage.py createsuperuser

Username (Required)
Email (Required)
Password (Required)

**After Superuser Login — Creating New Admin Users:**
Login to the Django Admin Panel using the superuser credentials.

Go to Users → Add User.

While adding a new user, make sure to:

Provide Username (Required)

Provide Email (Required)

Set Password (Required)

Check Is Admin (If applicable in your model)

Click Save.


6.**Run the Development Server:**
python manage.py runserver

7.**Access the App in Browser:**
Visitor Side: http://127.0.0.1:8000/
Admin Panel: http://127.0.0.1:8000/admin_login_view

References:
Django Documentation:https://docs.djangoproject.com/en/5.2/

Django Custom User Model:https://docs.djangoproject.com/en/5.2/topics/auth/customizing/#using-a-custom-user-model

Django Template Filters & Context Processors:https://docs.djangoproject.com/en/5.2/ref/templates/api/
