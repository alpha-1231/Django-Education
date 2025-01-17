import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example.settings")
django.setup()

from faker import Faker
from app.models import Person

# Initialize Faker and create dummy data
fake = Faker()

for _ in range(50):
    Person.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        birth_date=fake.date_of_birth(minimum_age=18, maximum_age=80),
    )

print("50 dummy records created successfully!")


    