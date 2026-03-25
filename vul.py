import sqlite3

def get_user_by_id(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # ❌ VULNERABILITY: SQL Injection
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)

    result = cursor.fetchall()
    conn.close()
    return result


if __name__ == "__main__":
    user_input = input("Enter user id: ")
    print(get_user_by_id(user_input))
``