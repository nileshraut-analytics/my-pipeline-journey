import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host = "localhost",
    database = "Practice_database",
    user = "postgres",
    password = "Nilesh0424"
)

# cursor = conn.cursor()
# cursor.execute("SELECT product, SUM(amount) FROM sales GROUP BY product")
# rows = cursor.fetchall()
# df = pd.DataFrame(rows, columns=["product", "amount"])

query = "SELECT * FROM sales"
df = pd.read_sql(query, conn)
print(df)

