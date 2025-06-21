from threading import Lock

# Singleton 
class DatabaseManager:
    _instance = None
    _lock = Lock()
    
    def __init__(self):
        self.databases = {}

    def create_database(self, database):
        if database.name in self.databases.keys():
            raise Exception("DataBase already exist!")
        
        self.databases[database.name] = database
        print(f"Database {database.name} created!")

    
    def create_db_table(self, db_name, table):
        db = self.databases.get(db_name)
        db.create_table(table)
        self.databases[db_name] = db

    @staticmethod
    def get_instance(): # double check locking
        if DatabaseManager._instance is None:
            with DatabaseManager._lock:
                if DatabaseManager._instance is None:
                    DatabaseManager._instance = DatabaseManager()
        return DatabaseManager._instance