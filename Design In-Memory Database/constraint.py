from abc import ABC, abstractmethod
from Helper.constants import MAX_LENGTH, MIN_INT_VAL, MAX_INT_VAL

class Contraint(ABC):
    
    @abstractmethod
    def validate():
        pass

class MaxLenConstraint(Contraint):
    def __init__(self, max_len=MAX_LENGTH):
        self._max_len = max_len

    def validate(self, value):
        if len(value) <= self._max_len:
            return True
        raise Exception("Max Len Contraint Failed!")


class RangeContraint(Contraint):
    def __init__(self, min_val=MIN_INT_VAL, max_val=MAX_INT_VAL):
        self._max_val = max_val
        self._min_val = min_val

    def validate(self, value):
        if value <= self._max_val and value >= self._min_val:
            return True
        raise Exception("Range Contraint Failed!")