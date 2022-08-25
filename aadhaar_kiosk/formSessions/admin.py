from django.contrib import admin
from aadhaar_kiosk.formSessions.models import enrolForm

class enrolFormAdmin(admin.ModelAdmin):
    pass
admin.site.register(enrolForm, enrolFormAdmin)
