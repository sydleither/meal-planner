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