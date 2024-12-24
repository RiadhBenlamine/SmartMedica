import random
from faker import Faker

from doctors_portal.models import Doctor, Patient 

fake = Faker()

def create_fake_doctors(count=10):
    GENDERS = ['male', 'female']
    SPECIALITIES = [
        'cardiologist', 'neurologist', 'general practitioner',
        'dermatologist', 'pediatrician', 'surgeon'
    ]

    for _ in range(count):
        Doctor.objects.create(
            fullname=fake.name(),
            gender=random.choice(GENDERS),
            phone_number=fake.phone_number(),
            speciality=random.choice(SPECIALITIES),
        )

def create_fake_patients(count=50):
    GENDERS = ['male', 'female']
    RELATIONSHIPS = ['single', 'married', 'divorced', 'widow']
    BLOOD_GROUPS = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

    for _ in range(count):
        Patient.objects.create(
            fullname=fake.name(),
            gender=random.choice(GENDERS),
            birthday=fake.date_of_birth(minimum_age=1, maximum_age=99),
            address=fake.address(),
            phone_number=fake.phone_number(),
            relationship=random.choice(RELATIONSHIPS),
            blood=random.choice(BLOOD_GROUPS),
            notes=fake.text(max_nb_chars=200),
        )

def main():
    create_fake_doctors(count=10) 
    create_fake_patients(count=50)  
    print("Fake data creation completed.")

if __name__ == "__main__":
    main()
