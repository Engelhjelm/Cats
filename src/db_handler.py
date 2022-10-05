#!/usr/bin/python3.9
import sqlite3

def create_db_table() -> bool:
    result = False
    try:
        dBConn = connect_to_db()
        dBConn.execute('''
            CREATE TABLE content (
                id INTEGER PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                description TEXT NOT NULL
            );
        ''')

        dBConn.commit()
        print("Table created successfully")
        result = True
    except:
        print("Table creation failed")
    finally:
        dBConn.close()
        return result



def connect_to_db():
    dBConnection = sqlite3.connect('database')
    return dBConnection


def get_content():
    content = []
    try:
        dBConnection = connect_to_db()
        dBConnection.row_factory = sqlite3.Row
        current = dBConnection.cursor()
        current.execute("SELECT * FROM content")
        rows = current.fetchall()

        # convert row objects to dictionary
        for i in rows:
            elements = {}
            elements["id"] = i["id"]
            elements["name"] = i["name"]
            elements["description"] = i["description"]
            content.append(elements)

    except:
        content = []

    return content


def create_content(content):
    inserted_content = {}
    try:
        dB = connect_to_db()
        current = dB.cursor()
        current.execute("INSERT INTO content (name, description) \
                     VALUES (?, ?)",
                     (content['name'], content['description']))
        dB.commit()
        temp_content = current.execute("SELECT * FROM content ORDER BY id DESC LIMIT 1")
        inserted_content = temp_content.fetchone()
    except:
        dB().rollback()

    finally:
        dB.close()

    return inserted_content
