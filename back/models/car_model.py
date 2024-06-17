import pyodbc

connection_str = """DRIVER={SQL Server};
        SERVER=MYCOMP;
        DATABASE=carStore"""


def get_all_cars():
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()
        query = "select * from cars"
        cursor.execute(query)
        return cursor.fetchall()


def get_car_by_id(car_id):
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()
        query = f"select * from cars where car_id = '{car_id}'"
        cursor.execute(query)
        return cursor.fetchone()


def create_car(new_car):
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()
        if new_car:
            if 'car_pic' not in new_car:
                new_car['car_pic'] = 'NONE'
            query = """INSERT INTO cars (model, color, manufacturer, manufacturer_date, license_num, price, num_seats, car_pic) 
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
            values = (
                new_car['model'],
                new_car['color'],
                new_car['manufacturer'],
                new_car['manufacturer_date'],
                new_car['license_num'],
                new_car['price'],
                new_car['num_seats'],
                new_car['car_pic'])
            cursor.execute(query, values)
            return {'status': 'success', 'message': 'Car added successfully', 'new car': new_car}
        else:
            return {'error': 'Car is undefined'}


def update_car(updated_car):
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()
        if updated_car:
            # Ensure car_pic has a default value if not provided
            if 'car_pic' not in updated_car:
                updated_car['car_pic'] = 'NONE'

            update_query = """UPDATE cars SET model = ?, color = ?, manufacturer = ?, manufacturer_date = ?, license_num = ?, price = ?, num_seats = ?, car_pic = ?
                              WHERE car_id = ?"""
            values = (
                updated_car['model'],
                updated_car['color'],
                updated_car['manufacturer'],
                updated_car['manufacturer_date'],
                updated_car['license_num'],
                updated_car['price'],
                updated_car['num_seats'],
                updated_car['car_pic'],
                updated_car['car_id']
            )
            cursor.execute(update_query, values)
            connection.execute()
            return {'status': 'success', 'message': 'Car updated successfully', 'updated_car': updated_car}
        else:
            return {'error': 'Car is undefined'}


def delete_car(car_id):
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()
        query = f"delete from cars where car_id = '{car_id}'"
        cursor.execute(query)
        return {'status': 'success', 'message': 'Car deleted successfully'}


new_car = {
    'car_id': 2011,
    'model': 'Model d',
    'color': 'Red',
    'manufacturer': 2,
    'manufacturer_date': '2023-01-15',
    'license_num': 'dtr852C5423',
    'price': 30000,
    'num_seats': 5,
}

# result = update_car(new_car)
# print(result)
