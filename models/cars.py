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
        return cursor.fetchall()


def get_car_by_id(id):
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()
        query = f"select * from cars where car_id = '{id}'"
        cursor.execute((query))
        print(cursor.fetchone())
        return cursor.fetchone()


# def create_car(new_car):
#      with pyodbc.connect(connection_str) as connection:
#         cursor = connection.cursor()
#         if new_car:
#               query = """INSERT INTO cars (model, color, manufacturer, manufacturer_date, license_num, price, num_seats)
#                        VALUES (?, ?, ?, ?, ?, ?, ?)"""
#             values = (new_car.model, new_car.color, new_car.manufacturer, new_car.manufacturer_date, new_car.license_num, new_car.price, new_car.num_seats)
#             cursor.execute(query, values)
#         else:
#             return {'error:', 'car is undifined'}

def create_car(new_car):
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()
        if new_car:
            query = """INSERT INTO cars (model, color, manufacturer, manufacturer_date, license_num, price, num_seats) 
                       VALUES (?, ?, ?, ?, ?, ?, ?)"""
            values = (new_car['model'], new_car['color'], new_car['manufacturer'], new_car['manufacturer_date'],
                      new_car['license_num'], new_car['price'], new_car['num_seats'])
            cursor.execute(query, values)
            return {'status': 'success', 'message': 'Car added successfully', 'new car': new_car}
        else:
            return {'error': 'Car is undefined'}


def update_car(updated_car):
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()
        if updated_car:
            update_query = """UPDATE cars SET model = ?, color = ?, manufacturer = ?, manufacturer_date = ?, license_num = ?, price = ?, num_seats = ?
                              WHERE car_id = ?"""
            values = (updated_car['model'], updated_car['color'], updated_car['manufacturer'], updated_car['manufacturer_date'], updated_car['license_num'], updated_car['price'], updated_car['num_seats'], updated_car['car_id'])
            cursor.execute(update_query, values)
            return {'status': 'success', 'message': 'Car updated successfully', 'update car': updated_car}
        else:
            return {'error': 'Car is undefined'}


new_car = {
    'car_id': 5,
    'model': 'Model S',
    'color': 'Red',
    'manufacturer': 2,
    'manufacturer_date': '2023-01-15',
    'license_num': 'ABC123',
    'price': 30000,
    'num_seats': 5
}
result = update_car(new_car)
print(result)
