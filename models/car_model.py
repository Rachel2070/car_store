import pyodbc



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
            if 'color' not in new_car:
                new_car['color'] = 'NONE'
            if 'manufacturer_date' not in new_car:
                new_car['manufacturer_date'] = 'NONE'
            if 'num_seats' not in new_car:
                new_car['num_seats'] = 'NONE'
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
            connection.commit()
            return {'status': 200, 'message': 'Car updated successfully', 'updated_car': updated_car}
        else:
            return {'error': 'Car is undefined'}

def delete_car(car_id):
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()
        query = f"delete from cars where car_id = '{car_id}'"
        cursor.execute(query)
        return {'status': 'success', 'message': 'Car deleted successfully'}


def get_manufacturer_id(cursor, manufacturer_name):
    query = "SELECT manufacturer_id FROM manufacturers WHERE manufacturer_name = ?"
    cursor.execute(query, (manufacturer_name,))
    result = cursor.fetchone()
    return result[0] if result else None

def search_car(parameters):
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()
        man = parameters.get('manufacturer', 'Manufacturer')
        model = parameters.get('model', '')
        price = parameters.get('price', '')

        conditions = []
        values = []

        if man != 'Manufacturer':
            manufacturer_id = get_manufacturer_id(cursor, man)
            if manufacturer_id:
                conditions.append("manufacturer = ?")
                values.append(manufacturer_id)
            else:
                print("Manufacturer not found")
                return []

        if model:
            conditions.append("model = ?")
            values.append(model)
        if price:
            conditions.append("price <= ?")
            values.append(price)

        query = "SELECT * FROM cars"
        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        print(query)  # For debugging purposes
        cursor.execute(query, values)
        results = cursor.fetchall()
        
        return results




# obj = {'manufacturer': 'Toyota', 'model':'', 'price':50000000000}
# res = search_car(obj)
# print(res)


# new_car = {
#     'car_id': 2011,
#     'model': 'Model d',
#     'manufacturer': 2,
#     'manufacturer_date': '2023-01-15',
#     'license_num': 'dtr882C5423',
#     'price': 30000,
#     'num_seats': 5,
# }

# result = create_car(new_car)
# print(result)
