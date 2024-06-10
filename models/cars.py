import pyodbc


connection_str = """DRIVER={SQL Server};
        SERVER=MYCOMP;
        DATABASE=carStore"""


def get_all_cars():
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()
        query = "select * from cars"
        cursor.execute((query))
        print(cursor.fetchall())


