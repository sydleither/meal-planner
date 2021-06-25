import sqlite3


def add_ingredients_to_database(ingredients):
    con = sqlite3.connect('model/database.db')
    cur = con.cursor()
    
    ingredient_ids = []
    for ingredient in ingredients:
        if not is_duplicate(ingredient.name):
            cur.execute('INSERT INTO ingredient VALUES (NULL,?,?)', (ingredient.name, ingredient.note))
            cur.execute('SELECT last_insert_rowid();')
            ingredient_ids.append(cur.fetchone()[0])
        else:
            ingredient_ids.append(is_duplicate(ingredient.name, True))
    
    con.commit()
    con.close()
    return ingredient_ids


def is_duplicate(ingredient_name, return_id=False):
    con = sqlite3.connect('model/database.db')
    cur = con.cursor()
    row = cur.execute('SELECT * FROM ingredient WHERE name=?', (ingredient_name,)).fetchone()
    if row and not return_id:
        return True
    elif row and return_id:
        return row[0]
    return False