from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def set_roll_no(self, roll_no):
        pass

    @abstractmethod
    def set_f_name(self, f_name):
        pass

    @abstractmethod
    def set_m_name(self, m_name):
        pass

    @abstractmethod
    def set_age(self, age):
        pass

    @abstractmethod
    def set_subjects(self, subjects):
        pass

    @abstractmethod
    def build(self):
        pass