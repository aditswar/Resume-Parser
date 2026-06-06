import psycopg2

def insert_candidate(name, email, phone, skills):
    conn = psycopg2.connect(
        host="localhost",
        database="resume_parser",
        user="postgres",
        password="800014"
    )

    cur = conn.cursor()

    cur.execute("""
        INSERT INTO candidates(name, email, phone, skills)
        VALUES (%s, %s, %s, %s)
    """, (name, email, phone, skills))

    conn.commit()

    cur.close()
    conn.close()