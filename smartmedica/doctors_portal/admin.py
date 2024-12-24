from django.contrib import admin
from .models import Doctor, Patient, Visit
# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'date_joined', 'phone_number', 'speciality', 'gender')
    search_fields = ('fullname', 'phone_number', 'speciality')
    list_filter = ('speciality',)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'relationship', 'blood', 'phone_number', 'first_visit', 'last_visit', 'gender')
    search_fields = ('fullname', 'phone_number', 'relationship', 'blood', 'gender', 'last_visit')

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'visit_date', 'reason')
    search_fields = ('patient', 'doctor', 'visit_date', 'reason')
    list_filter = ('visit_date', 'reason', 'doctor')