import os
import django
from faker import Faker

# Set the correct settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'example.settings')
django.setup()

from app.models import UserData  # Ensure 'app' matches your Django app name
# Create a Faker instance
fake = Faker()

# Generate and insert 50 dummy records
users = []
for _ in range(50):
    users.append(UserData(name=fake.name(), age=fake.random_int(min=18, max=60)))

# Bulk insert for better performance
UserData.objects.bulk_create(users)

print("50 dummy user records have been created successfully!")
