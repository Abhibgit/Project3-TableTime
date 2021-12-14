from django.contrib import admin
from .models import Profile
from .models import Restaurant, Reviews, Reservations

# Register your models here.
# admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Profile)
admin.site.register(Reviews)
admin.site.register(Reservations)

