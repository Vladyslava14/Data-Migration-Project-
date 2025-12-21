import psycopg2

CHECKS = {
    "missing_fields": """
        SELECT COUNT(*) 
        FROM customer
        WHERE first_name IS NULL OR phone IS NULL;
    """,
    "invalid_phone": """
        SELECT COUNT(*) 
        FROM customer
        WHERE length(phone) < 10;
    """,
    "future_birthdates": """
        SELECT COUNT(*) 
        FROM customer
        WHERE birthdate > CURRENT_DATE;
    """,
}

def run_checks():
    conn = psycopg2.connect(
        dbname="Target_db",
        user="postgres",
        password="...",
        host="localhost",
        port=5432
    )
    cur = conn.cursor()

    print("DATA QUALITY REPORT")
    print("----------------------")

    for name, query in CHECKS.items():
        cur.execute(query)
        count = cur.fetchone()[0]
        print(f"{name}: {count}")

    cur.close()
    conn.close()

if __name__ == "__main__":
    run_checks()
