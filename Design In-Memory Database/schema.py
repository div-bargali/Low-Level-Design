class Schema:
    def __init__(self, columns):
        # {columns_name: column_obj}
        self._columns = columns

    def validate_schema(self, row):
        for column_name, value in row.items():
            if column_name not in self._columns:
                raise Exception(f"Column {column_name} is not defined")

            column_obj = self._columns[column_name]
            if not column_obj.validate(value):
                raise Exception(f"Column validation failed for {column_name}")
        return True