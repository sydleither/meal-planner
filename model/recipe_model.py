import sqlite3


def add_recipe_to_database(recipe):
    con = sqlite3.connect('model/database.db')
    cur = con.cursor()
    
    cur.execute('INSERT INTO recipe VALUES (NULL,?,?,?,?,?,?,?)', \
                 (recipe.name, recipe.instructions, recipe.meal_type, \
                  recipe.subtype, recipe.servings, recipe.vegan, 0))
        
    cur.execute('SELECT last_insert_rowid();')
    recipe_id = cur.fetchall()[0][0]
    
    con.commit()
    con.close()
    
    return recipe_id