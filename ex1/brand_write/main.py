import os
import psycopg2

from flask import Flask, render_template, request

app = Flask(__name__)

db_name = os.environ["DB_NAME"]

conn = psycopg2.connect(
    database=db_name,
    host=os.environ["DB_HOST"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASS"],
    port=os.environ["DB_PORT"]
)

conn.autocommit = True
with conn.cursor() as cursor:
    cursor.execute("create table if not exists brands (name VARCHAR(50));")


@app.route("/", methods=["GET", "POST"])
def create():
    brand = None
    if request.method == "POST":
        brand = request.form["brand"]
        with conn.cursor() as cursor:
            cursor.execute(f"insert into brands(name) values ('{brand}');")

    context = {
        "brand": brand
    }

    return render_template("index.html", **context)


app.run(host='0.0.0.0', port=8002, debug=True)
