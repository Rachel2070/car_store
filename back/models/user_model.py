import pyodbc

connection_str = """DRIVER={SQL Server};
        SERVER=MYCOMP;
        DATABASE=carStore"""


def get_all_users():
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()
        query = "select * from users"
        cursor.execute(query)
        return cursor.fetchall()


def get_user_by_id(user_id):
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()
        query = f"select * from users where user_id = '{user_id}'"
        cursor.execute(query)
        return cursor.fetchone()


def create_user(new_user):
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()
        if new_user:
            if 'credit_card' not in new_user:
                new_user['credit_card'] = 'NONE'
            if 'user_age' not in new_user:
                new_user['user_age'] = 'NONE'
            query = """INSERT INTO users (user_name, user_address, user_email, credit_card, user_age) 
                       VALUES (?, ?, ?, ?, ?)"""
            values = (
                new_user['user_name'],
                new_user['user_address'],
                new_user['user_email'],
                new_user['credit_card'],
                new_user['user_age'])
            cursor.execute(query, values)
            return {'status': 'success', 'message': 'User added successfully', 'new user': new_user}
        else:
            return {'error': 'User is undefined'}


def update_user(updated_user):
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()
        if updated_user:
            if 'credit_card' not in updated_user:
                updated_user['credit_card'] = 'NONE'
            if 'user_age' not in updated_user:
                updated_user['user_age'] = 'NONE'

            update_query = """UPDATE users SET user_name = ?, user_address = ?, user_email = ?, credit_card = ?, user_age = ?
                              WHERE user_id = ?"""
            values = (
                updated_user['user_name'],
                updated_user['user_address'],
                updated_user['user_email'],
                updated_user['credit_card'],
                updated_user['user_age'],
                updated_user['user_id']
            )
            cursor.execute(update_query, values)
            return {'status': 'success', 'message': 'User updated successfully', 'updated_user': updated_user}
        else:
            return {'error': 'User is undefined'}


def delete_user(user_id):
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()
        query = f"delete from users where user_id = '{user_id}'"
        cursor.execute(query)
        return {'status': 'success', 'message': 'User deleted successfully'}

new_user = {
    'user_id': 100,
    'user_name': 'ddo bbb',
    'user_address': '1gg3 nain St',
    'user_email': 'john.doe@example.com',
    'user_age': 30
}

# result = get_user_by_id(100)
# print(result)
