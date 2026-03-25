import sqlite3

def get_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # ❌ SQL Injection vulnerability (CodeQL WILL flag this)
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)

    rows = cursor.fetchall()
    conn.close()
    return rows


if __name__ == "__main__":
    uid = input("Enter user id: ")
    print(get_user(uid))