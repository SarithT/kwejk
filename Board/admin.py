from django.contrib import admin
from Board.models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'description', 'date', 'addedBy', 'isOnGifMonitor')

admin.site.register(Image, ImageAdmin)
