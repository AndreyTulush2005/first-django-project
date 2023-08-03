from django.contrib import admin

from .models import Advertisement

# Register your models here.


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'created_at', 'update_at', 'auction']
    list_filter = ['auction']


admin.site.register(Advertisement, AdvertisementAdmin)

