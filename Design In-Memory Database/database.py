class Database:
    def __init__(self, database_name):
        self.name = database_name
        self.tables = {}
        self.table_id = 1


    def create_table(self, table):
        if table.name in self.tables.keys():
            raise Exception("Table Name already exist!")
        
        self.tables[table.name] = table
        print(f"Table {table.name} created!")

    