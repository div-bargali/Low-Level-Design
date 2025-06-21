class Column:
    def __init__(self, name, data_type, is_req=False, constraints=None):
        self._name = name
        self._data_type = data_type
        self._is_required = is_req
        self._constraints = constraints if constraints is not None else []

    def add_contraints(self, constraint):
        self._constraints.append(constraint)

    def validate(self, value):
        # validate datatype
        if not isinstance(value, self._data_type):
            raise Exception(f"Value for column {self._name} must be of type {self._data_type}!")
        
        # validate is_required constraint
        if value is None and self._is_required:
            raise Exception(f"Value for column {self._name} can not be None!")

        for constraint in self._constraints:
            constraint.validate(value)
        return True