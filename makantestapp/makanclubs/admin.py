from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Club)
admin.site.register(Eater)
admin.site.register(Location)
admin.site.register(Experience)
admin.site.register(Membership)