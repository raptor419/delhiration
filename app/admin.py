# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

from .models import *
admin.site.register(CircleNumber)
admin.site.register(FPShop)
admin.site.register(RationCard)
admin.site.register(Locality)
admin.site.register(Collection)
admin.site.register(Ration)


