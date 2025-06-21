class Table:
    def __init__(self, table_name, schema):
        self.name = table_name
        self.rows = {} # Dict {row_id: {column_name1: column_val1, ...}}
        self.schema = schema
        self.auto_id = 0

    def insert(self, row):
        if self.schema.validate_schema(row):
            self.rows[self.auto_id] = row
            self.auto_id += 1
            print(f"Insert record at id {self.auto_id}")

    # update table __ set __ where id = __
    def update(self, row_id, new_row):
        if self.schema.validate_schema(row):
            update_row = self.rows[row_id]
            for column_name, new_val in new_row.items():
                update_row[column_name] = new_val
            self.rows[row_id] = update_row

    def query(self, filters):
        result = []
        for row_id, row in self.rows.items():
            for column_name, column_val in filters.items():
                if row[column_name] == column_val:
                    result.append(row)
        return result 
        

    