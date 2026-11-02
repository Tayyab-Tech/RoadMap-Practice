
from database import get_connection

try:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    current_database(),
                    current_user,
                    version()
            """)

            database, user, version = cur.fetchone()

            print("Connected to Neon successfully!")
            print("Database:", database)
            print("User:", user)
            print("Server:", version.split(",")[0])

except Exception as error:
    print("Connection failed:", error)
