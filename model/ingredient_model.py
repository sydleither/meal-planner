import sqlite3


def add_ingredients_to_database(ingredients):
    con = sqlite3.connect('model/database.db')
    cur = con.cursor()
    
    ingredient_ids = []
    for ingredient in ingredients:
        cur.execute('INSERT INTO ingredient VALUES (NULL,?,?)', (ingredient.name, ingredient.note))
        cur.execute('SELECT last_insert_rowid();')
        ingredient_ids.append(cur.fetchall()[0][0])
    
    con.commit()
    con.close()
    
    return ingredient_ids


def is_duplicate(ingredient_name):
    con = sqlite3.connect('model/database.db')
    cur = con.cursor()
    row = cur.execute('SELECT * FROM ingredient WHERE name=?', (ingredient_name,))
    if row.fetchone():
        return True
    return False
    
    