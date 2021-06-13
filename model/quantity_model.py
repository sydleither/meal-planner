import sqlite3


def add_quantities_to_database(quantities):
    con = sqlite3.connect('model/database.db')
    cur = con.cursor()
    
    for quantity in quantities:
        values = (quantity.recipe_id, quantity.ingredient_id, \
                  quantity.amount, quantity.measurement, quantity.note)
        cur.execute('INSERT INTO quantity VALUES (NULL,?,?,?,?,?)', values)
    
    con.commit()
    con.close()