from . abstract_model import  Name 
from . abstract_related import Base 



class Student(Name):
    class Meta:
        db_table="Student"
        

class ChildA(Base):
    pass

class ChildB(Base):
    pass 
