import os
import django
from django.db import connection
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example.settings")
django.setup()

from app.models import Person 

# a=Person.objects.raw("SELECT * FROM app_person")
# for i in a:
#     print(f"Hi i am {i.first_name} {i.last_name} and i am from the year {i.birth_date}")  

# a =  Person.objects.raw("SELECT id,first_name as F,last_name from app_person")
# for i in a:
#     print(i.first_name)
    
# a =  Person.objects.raw("SELECT id,first_name as F,last_name from app_person LIMIT 10")
# b=1
# for i in a:
    
#     print(b," ",i.first_name)
#     b+=1
    
def my_custom_sql():
    with connection.cursor() as cursor:
        a=cursor.execute("SELECT * FROM app_person")
        # for i in a:
        #     print(f"Hi i am {i[1]} {i[2]} and i am from the year {i[3]}")  
            # print(i)
        # print(cursor.fetchone())
        # print(cursor.fetchmany(10))
        # print(cursor.fetchall())
        

my_custom_sql()
