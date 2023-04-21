"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch13ak3h4hstbhh8npeg-a.oregon-postgres.render.com",
        database="todo_cq73",
        user="todo_cq73_user",
        password="AhMWZSrxoAsv9g1WFftRo7RH6kHh0NQ7")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
