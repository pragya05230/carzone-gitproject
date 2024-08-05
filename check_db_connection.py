import psycopg2

try:
    conn = psycopg2.connect(
        dbname='carzone_db',
        user='postgres',
        password='2305',  # Replace with your actual password
        host='localhost'
    )
    cur = conn.cursor()
    cur.execute('SHOW timezone;')
    timezone = cur.fetchone()
    print(f"Database timezone: {timezone}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if conn:
        cur.close()
        conn.close()
