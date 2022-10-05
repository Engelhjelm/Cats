#!/usr/bin/python3.9

from db_handler import create_content, create_db_table

content = []

no1 = { "name" : "cat",
        "description" : "Short for concatenate, very useful terminal command"}
no2 = { "name" : "Garfield",
        "description": "Lazy red cat who loves lasagna"}
no3 = { "name" : "Cats",
        "description" : "Multiple instances of the animal cat" }
content.append(no1)
content.append(no2)
content.append(no3)

if create_db_table():
    for i in content:
            print(create_content(i))