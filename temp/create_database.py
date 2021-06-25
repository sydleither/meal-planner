#this is a temp file not connected to overall project structure. leaving it here while developing
import sqlite3


con = sqlite3.connect('../model/database.db') #TODO better name
cur = con.cursor()

cur.execute('''CREATE TABLE recipe (
    recipe_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    link TEXT,
    instructions TEXT,
    meal_type TEXT,
    subtype TEXT,
    servings NUMERIC,
    vegan INTEGER
    );''')
cur.execute('''CREATE TABLE ingredient (
    ingredient_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    note TEXT
    );''')
cur.execute('''CREATE TABLE quantity (
    quantity_id INTEGER PRIMARY KEY,
    recipe_id INTEGER NOT NULL,
    ingredient_id INTEGER NOT NULL,
    amount REAL,
    measurement TEXT,
    note TEXT
    );''')
cur.execute('''CREATE TABLE planner (
    planner_id INTEGER PRIMARY KEY,
    meal TEXT NOT NULL,
    monday TEXT,
    tuesday TEXT,
    wednesday TEXT,
    thursday TEXT,
    friday TEXT,
    saturday TEXT,
    sunday TEXT
    );''')

con.commit()
con.close()