from django.contrib import admin
from .models import Image
#from easy_thumbnails import fields, widgets


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']
    #formfield_overrides = {
    #    fields.ThumbnailerField: {'widget': widgets.ImageClearableFileInput},
    #}
