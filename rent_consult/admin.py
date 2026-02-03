from django.contrib import admin

# Register your models here.
from .models import ConsultationRequest

admin.site.register(ConsultationRequest)