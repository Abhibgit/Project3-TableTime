from django.contrib import admin
from .models import Profile
from .models import Restaurant

# Register your models here.
# admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Profile)
