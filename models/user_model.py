import pyodbc


def login(username, user_password):
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()

        # Check if the username exists
        user_query = "SELECT user_id, password FROM users WHERE user_name = ?"
        cursor.execute(user_query, (username,))
        user = cursor.fetchone()

        if user:
            user_id, password = user
            if password == user_password:
                return {'status': 200, 'user': user}
            else:
                return {'status': 400, 'message': 'Password does not match'}
        else:
            return {'status': 404, 'message': 'User does not exist'}


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
            query = """INSERT INTO users (user_name, user_address, user_email, credit_card, user_age, password) 
                       VALUES (?, ?, ?, ?, ?, ?)"""
            values = (
                new_user['user_name'],
                new_user['user_address'],
                new_user['user_email'],
                new_user['credit_card'],
                new_user['user_age'],
                new_user['password'])
            cursor.execute(query, values)
            return {'status': 200, 'message': 'User added successfully', 'new user': new_user}
        else:
            return {'status': 401}


def update_user(updated_user):
    with pyodbc.connect(connection_str) as connection:
        cursor = connection.cursor()
        if updated_user:
            if 'credit_card' not in updated_user:
                updated_user['credit_card'] = 'NONE'
            if 'user_age' not in updated_user:
                updated_user['user_age'] = 'NONE'

            update_query = """UPDATE users SET user_name = ?, user_address = ?, user_email = ?, credit_card = ?, user_age = ?, password =?
                              WHERE user_id = ?"""
            values = (
                updated_user['user_name'],
                updated_user['user_address'],
                updated_user['user_email'],
                updated_user['credit_card'],
                updated_user['user_age'],
                updated_user['password'],
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
    'user_name': 'gdzgfggggg bbb',
    'user_address': '1gg3 nain St',
    'user_email': 'ohn.o@example.com',
    'user_age': 30,
    'password': '68dfaa3g'
}

# result = login('ggggggggggg bbb', '68f3g')
# print(result)
# print(get_all_users())
