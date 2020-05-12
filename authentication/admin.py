# -*- encoding: utf-8 -*-


from django.contrib import admin

# Register your models here.

from authentication.models import User
admin.site.register(User)


