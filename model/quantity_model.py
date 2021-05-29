import sqlite3


def add_quantities_to_database(quantities):
    con = sqlite3.connect('model/database.db')
    cur = con.cursor()
    
    quantity_ids = []
    for quantity in quantities:
        values = (quantity.recipe_id, quantity.ingredient_id, \
                  quantity.amount, quantity.measurement, quantity.note)
        cur.execute('INSERT INTO quantity VALUES (NULL,?,?,?,?,?)', values)
        cur.execute('SELECT last_insert_rowid();')
        quantity_ids.append(cur.fetchall()[0][0])
    
    con.commit()
    con.close()
    
    return quantity_ids