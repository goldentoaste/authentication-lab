from django.contrib import admin

# Register your models here.
from rest_framework.authtoken.admin import TokenAdmin
from rest_framework.authtoken.models import Token

TokenAdmin.raw_id_fields = ('user',)