from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DATABASE_HOST"),
            port=os.getenv("DATABASE_PORT"),
            database=os.getenv("DATABASE_DB"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD")
        )

        conn.close()

        return "App connected to PostgreSQL successfully!"

    except Exception as e:
        return f"Database connection failed: {e}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)