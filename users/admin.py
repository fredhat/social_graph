from django.contrib import admin
from .models import User, Follows

admin.site.register(User)
admin.site.register(Follows)