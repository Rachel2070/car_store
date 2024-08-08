import pyodbc


def get_all_manufacturers():
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()
        query = "select * from manufacturers"
        cursor.execute(query)
        return cursor.fetchall()


def get_manufacturer_by_id(manufacturer_id):
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()
        query = f"select * from manufacturers where manufacturer_id = '{manufacturer_id}'"
        cursor.execute(query)
        return cursor.fetchone()


def create_manufacturer(new_manufacturer):
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()
        if new_manufacturer:
            if 'manufacturer_country' not in new_manufacturer:
                new_manufacturer['manufacturer_country'] = 'NONE'
            query = """INSERT INTO manufacturers (manufacturer_name, business_num, manufacturer_country) 
                       VALUES (?, ?, ?)"""
            values = (
                new_manufacturer['manufacturer_name'],
                new_manufacturer['business_num'],
                new_manufacturer['manufacturer_country'],
            )
            cursor.execute(query, values)
            return {'status': 'success', 'message': 'Manufacturer added successfully', 'new user': new_manufacturer}
        else:
            return {'error': 'Manufacturer is undefined'}


def update_manufacturer(updated_manufacturer):
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()
        if updated_manufacturer:
            if 'manufacturer_country' not in updated_manufacturer:
                updated_manufacturer['manufacturer_country'] = 'NONE'
            update_query = """UPDATE manufacturers SET manufacturer_name = ?, business_num = ?, manufacturer_country = ?
                              WHERE manufacturer_id = ?"""
            values = (
                updated_manufacturer['manufacturer_name'],
                updated_manufacturer['business_num'],
                updated_manufacturer['manufacturer_country'],
                updated_manufacturer['manufacturer_id'],
            )
            cursor.execute(update_query, values)
            return {'status': 'success', 'message': 'Manufacturer updated successfully',
                    'updated_user': updated_manufacturer}
        else:
            return {'error': 'Manufacturer is undefined'}


def delete_manufacturer(manufacturer_id):
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()
        query = f"delete from manufacturers where manufacturer_id = '{manufacturer_id}'"
        cursor.execute(query)
        return {'status': 'success', 'message': 'Manufacturer deleted successfully'}


new_manufacturer = {
    'manufacturer_id': 4,
    'manufacturer_name': 'porch',
    'business_num': '123476790',
    'manufacturer_country': 'USA'
}

# result = get_all_manufacturers()
# print(result)
