from django.contrib import admin
from django.contrib.auth.hashers import make_password
from events.models import CustomUser, Events, Booking

class CustomUserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data and not change:
            obj.password = make_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Events)
admin.site.register(Booking)