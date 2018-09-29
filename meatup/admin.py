from django.contrib import admin

# Register your models here.
from .models import Profile
from .models import Event
from .models import User


admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(User)
