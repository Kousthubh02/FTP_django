from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

from django.apps import apps

# Get all models from the current app
app = apps.get_app_config('testingApp')

# Register each model with the admin site
for model_name, model in app.models.items():
    admin.site.register(model)