# -*- encoding: utf-8 -*-


from django.contrib import admin

from app.models import *


class FPSInline(admin.TabularInline):
    model = FPS.user.through


@admin.register(FPS)
class FPSAdmin(admin.ModelAdmin):
    inlines = (FPSInline,)
    exclude = ('user',)
admin.site.register(Circle)
admin.site.register(RationCard)
admin.site.register(Locality)
admin.site.register(Collection)


