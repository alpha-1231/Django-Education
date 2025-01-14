import os
import django

# Set the correct Django settings module
os.environ["DJANGO_SETTINGS_MODULE"] = "example.settings"

# Initialize Django
django.setup()

from django.db import connections

# from app.models import User

# # Debugging: check if Django setup was successful
# print("Django is setup")

# # Try accessing the User model
# try:
#     user = User.objects.all()
#     print("Users in the database:", user)
# except Exception as e:
#     print("Error accessing the User model:", e)


# with connections['new'].cursor as cursor:
    # cursor.execute("SELECT * FROM info")
    # data = cursor.fetchall()
    # print(data)
    
# from django.db import connections

# # Open the connection and cursor manually
# cursor = connections['new'].cursor()

# try:
#     cursor.execute("SELECT * FROM info")
#     data = cursor.fetchall()
#     print(data)
# finally:
#     cursor.close()  # Ensure the cursor is closed after the operation
