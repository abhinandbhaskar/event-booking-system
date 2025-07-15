from django.contrib import admin

from events.models import CustomUser,Events,Booking

admin.site.register(CustomUser)
admin.site.register(Events)
admin.site.register(Booking)