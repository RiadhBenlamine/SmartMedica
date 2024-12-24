from django.test import TestCase
from faker import Faker
from faker.providers import DynamicProvider
from .models import Doctor, Patient, Visit


medical_professions_provider = DynamicProvider(
     provider_name="medical_profession",
     elements=["dr.", "doctor", "nurse", "surgeon", "clerk"],
)
fake = Faker()
fake.add_provider(medical_professions_provider)

class DoctorTestCase(TestCase):
    def setUp(self):
        self.doctor = Doctor.objects.create(
            fullname=fake.name_female(),
            gender="Female",
            speciality=fake.medical_profession(), 
            phone_number = '0556699815'        
        )

    def test_doctor_str(self):
        self.assertEqual(str(self.doctor), f'{self.doctor.fullname}')
