"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv

with psycopg2.connect(host="localhost", database="north", user="postgres", password="123456789") as conn:
    with conn.cursor() as cur:
        with open('../homework-1/north_data/customers_data.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    cur.execute('INSERT INTO customers VALUES (%s, %s, %s)',
                                (row["customer_id"], row["company_name"], row["contact_name"]))
                except Exception:
                    continue

    with conn.cursor() as cur:
        with open('../homework-1/north_data/employees_data.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                                (row["employee_id"], row["first_name"], row["last_name"], row["title"],
                                 row["birth_date"], row["notes"]))
                except Exception:
                    continue

    with conn.cursor() as cur:
        with open('../homework-1/north_data/orders_data.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)',
                                (row["order_id"], row["customer_id"], row["employee_id"], row["order_date"],
                                 row["ship_city"]))
                except Exception:
                    continue

conn.close()
