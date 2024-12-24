from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Doctor(models.Model):
    GENDERS = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    
    fullname = models.CharField(max_length=90)
    gender = models.CharField(choices=GENDERS, max_length=6)
    phone_number = PhoneNumberField()
    speciality = models.CharField(max_length=300)
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-date_joined',)
    
    def __str__(self):
        return self.fullname


class Patient(models.Model):
    RELATIONSHIPS = (
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widow', 'Widow'),
    )
    BLOOD_GROUPS = (
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    )
    GENDERS = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    fullname = models.CharField(max_length=90)
    gender = models.CharField(choices=GENDERS, max_length=6)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    address = models.CharField(max_length=250)
    phone_number = PhoneNumberField()
    relationship = models.CharField(choices=RELATIONSHIPS, max_length=11)
    blood = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    notes = models.TextField(null=True, blank=True)
    first_visit = models.DateTimeField(auto_now_add=True)
    last_visit = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.fullname

class Visit(models.Model):
    patient = models.ForeignKey(Patient, related_name="visits", on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name="doctor", on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
    notes = models.TextField()
    visit_summary = models.TextField(null=True, blank=True)
    visit_date = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return f"Visit #{self.pk} for {self.patient.fullname} with Dr. {self.doctor.fullname}"
