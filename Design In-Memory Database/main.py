from databasemanager import DatabaseManager
from database import Database
from column import Column
from constraint import MaxLenConstraint, RangeContraint
from schema import Schema
from table import Table

def main():
    """
    This is the main function of the project. It will create a database, a table in the database, insert a few rows and query the table.

    :return: None
    """
    db_manager = DatabaseManager.get_instance()

    # create the db
    db = Database("database1")
    db_manager.create_database(db)

    # create the column with contrains
    name_col = Column("user_name", str, True, [MaxLenConstraint()])
    age = Column("age", int, [RangeContraint(5, 120)])

    # define the schema
    schema = Schema({name_col._name: name_col, age._name: age})

    user_table = Table("users", schema)

    # create the table
    db_manager.create_db_table(db.name, user_table)

    # insert the data
    row = {"user_name": "Alice", "age": 10}
    user_table.insert(row)

    res = user_table.query({"age": 10})
    print(res)

    row2 = {"user_name": "Bob", "age": 10}
    user_table.insert(row)

    res = user_table.query({"age": 10})
    print(res)

if __name__ == "__main__":
    main()
