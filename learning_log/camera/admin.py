from django.contrib import admin

# Register your models here.
from camera.models import Camera, Model

admin.site.register(Camera)
admin.site.register(Model)
