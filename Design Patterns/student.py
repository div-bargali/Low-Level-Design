# this is the product class that the Builder class will make

class Student:
    def __init__(self, builder):
        self.roll_no = builder.roll_no
        self.name = builder.name
        self.f_name = builder.f_name
        self.m_name = builder.m_name
        self.age = builder.age
        self.subjects = builder.subjects

    def __repr__(self):
        return f"Student: {self.roll_no}, {self.name}, {self.age}"
