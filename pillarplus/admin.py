from django.contrib import admin
from . import models


admin.site.register(models.FileLoader)
admin.site.register(models.GoogleForm)