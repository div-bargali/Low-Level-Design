from builder import Builder
from student import Student

class EngineerBuider(Builder):
    def __init__(self):
        self.name = None
        self.roll_no = None
        self.f_name = None
        self.m_name = None
        self.age = None
        self.subjects = None

    def set_name(self, name):
        self.name = name
        return self

    def set_roll_no(self, roll_no):
        self.roll_no = roll_no
        return self 
    
    def set_age(self, age):
        self.age = age
        return self

    def set_f_name(self, f_name):
        self.f_name = f_name
        return self

    def set_m_name(self, m_name):
        self.m_name = m_name
        return self

    def set_subjects(self, subjects):
        if self.subjects is None:
            self.subjects = []
        self.subjects.append(subjects)
        return self

    def build(self):
        return Student(self)