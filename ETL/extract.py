import psycopg2

def extract():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="Legacy_db",
        user="postgres",
        password="..."
    )
    cur = conn.cursor()
    cur.execute("SELECT*FROM legacy_customer")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
print(extract())