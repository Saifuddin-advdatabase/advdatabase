# A very simple Bottle Hello World app for you to get started with...
import os
import sqlite3
from bottle import get, post, template, request, redirect

# are we executing at PythonAnywhere?
ON_PYTHONANYWHERE = "PYTHONANYWHERE_DOMAIN" in os.environ

assert ON_PYTHONANYWHERE == True

if ON_PYTHONANYWHERE:
    # on PA, set up to connect to the WSGI server
    from bottle import default_app
else:
    # on the development environment, import the development server
    from bottle import run, debug


@get('/')
def get_show_list():
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    #cursor.execute("select * from todo")
    cursor.execute("select * from covid")
    result = cursor.fetchall()
    cursor.close()
    return template("intro", rows=result)


# @get("/new_symtoms")
# def get_new_symtoms():
#     return template("new_symtoms")


# @post("/new_symtoms")
# def post_new_symtoms():
#     new_symtoms = request.forms.get("new_symtoms").strip()
#     connection = sqlite3.connect("todo.db")
#     cursor = connection.cursor()
#     cursor.execute("insert into intro (symtoms) VALUES (?)", (new_symtoms))
#     # cursor.lastrowid
#     connection.commit()
#     cursor.close()
#     #return "The new item is [" + new_item + "]..."
#     redirect("/")


@get("/new_symtoms")
def get_new_symtoms():
    return template("new_symtoms")


@post("/new_symtoms")
def post_new_symtoms():
    new_symtoms = request.forms.get("new_symtoms").strip()
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    print(cursor)
    #cursor.execute("INSERT INTO covid (symtoms) VALUES ('" + new_symtoms + "')")
    #cursor.execute("INSERT INTO covid (symtoms) VALUES (?)", (new_symtoms,))
    cursor.execute("INSERT INTO covid (symtoms) VALUES (?)", (new_symtoms,))
    # cursor.lastrowid
    connection.commit()
    cursor.close()
    #return "The new item is [" + new_item + "]..."
    redirect("/")


if ON_PYTHONANYWHERE:
    # on PA, connect to the WSGI server
    application = default_app()
else:
    # on the development environment, run the development server
    debug(True)
    run(host='localhost', port=8080)
