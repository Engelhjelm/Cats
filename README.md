# API for Cats
## Requirements:
* Python 3.9 or later version
* SQLite3 

## Setup the environment:
* `git clone <repo>`
* `cd <repo>`
* `pip install venv`
* `python3.9 -m venv .venv` to create your new environment (called '.venv' here)
* `source .venv/bin/activate` to enter the virtual environment
* `pip install -r requirements.txt` to install the requirements in the current environment

## How to run:
1. Then run `python3.9 ./src/create_and_fill_db_table.py` to create a database table and fill it with some dummy data.
2. Run `python3.9 ./app.py` to run the application on localhost:5000.
3. Open a web browser and  go to [cats/list](localhost:5000/cats/list) to send a GET request and list all items in the database.
4. Send a POST request with "name" and "description" in JSON format in the body [cats/create](localhost:5000/cats/create) to create new content to the database.
