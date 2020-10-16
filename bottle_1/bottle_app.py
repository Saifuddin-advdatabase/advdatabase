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


# Dear Professor, Greeting from <b> Saifuddin Mahmud</b>. I am very lucky to be a student of this
# course. I am also greatful to you as you are doing a great job for us. I never get a chance to work
#       in the industry but I am feeling now. <b>This web application is for Homework 2.</b>


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

@get("/update_symtoms")
def get_update_symtoms():
    return template("update_symtoms")

@post("/update_symtoms")
def post_update_symtoms():
    id = request.forms.get("id").strip()
    update_symtoms = request.forms.get("update_symtoms").strip()
    connection1 = sqlite3.connect("todo.db")
    cursor1 = connection1.cursor()
    print(cursor1)
    #cursor1.execute("INSERT INTO covid (symtoms) VALUES (?)", (update_symtoms,))
    cursor1.execute ("update covid set symtoms = (?) where id = (?) ",(update_symtoms,id))

    # cursor.lastrowid
    connection1.commit()
    cursor1.close()
    #return "The new item is [" + new_item + "]..."
    redirect("/")


@get("/delete_symtoms")
def get_delete_symtoms():
    return template("delete_symtoms")

@post("/delete_symtoms")
def post_delete_symtoms():
    id = request.forms.get("id").strip()
    connection1 = sqlite3.connect("todo.db")
    cursor1 = connection1.cursor()
    print(cursor1)
    #cursor1.execute("INSERT INTO covid (symtoms) VALUES (?)", (update_symtoms,))
    cursor1.execute ("delete from covid where id = (?) ",(id,))

    # cursor.lastrowid
    connection1.commit()
    cursor1.close()
    #return "The new item is [" + new_item + "]..."
    redirect("/")




if ON_PYTHONANYWHERE:
    # on PA, connect to the WSGI server
    application = default_app()
else:
    # on the development environment, run the development server
    debug(True)
    run(host='localhost', port=8080)
