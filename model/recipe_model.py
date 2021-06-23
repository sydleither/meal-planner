import sqlite3


def add_recipe_to_database(recipe):
    con = sqlite3.connect('model/database.db')
    cur = con.cursor()
    cur.execute('INSERT INTO recipe VALUES (NULL,?,?,?,?,?,?,?)', \
                 (recipe.name, recipe.link, recipe.instructions, recipe.meal_type, \
                  recipe.subtype, recipe.servings, recipe.vegan))
        
    cur.execute('SELECT last_insert_rowid();')
    recipe_id = cur.fetchone()[0]
    con.commit()
    con.close()
    return recipe_id


def get_all_recipes():
    con = sqlite3.connect('model/database.db')
    cur = con.cursor()
    query = 'SELECT recipe_id,name,link,meal_type,subtype,servings,vegan FROM recipe'
    rows = cur.execute(query).fetchall()
    return rows


def get_single_recipe(recipe_id):
    con = sqlite3.connect('model/database.db')
    cur = con.cursor()
    query = 'SELECT * FROM recipe r WHERE r.recipe_id=?'
    row = cur.execute(query, recipe_id).fetchone()
    return row


def get_single_recipe_name(recipe_id):
    con = sqlite3.connect('model/database.db')
    cur = con.cursor()
    query = 'SELECT name FROM recipe r WHERE r.recipe_id=?'
    row = cur.execute(query, recipe_id).fetchone()[0]
    return row


def get_recipe_ingredients(recipe_id):
    con = sqlite3.connect('model/database.db')
    cur = con.cursor()
    query = 'SELECT i.name, q.amount, q.measurement, q.note, i.note \
            FROM recipe r \
            JOIN quantity q ON r.recipe_id=q.recipe_id \
            JOIN ingredient i ON i.ingredient_id = q.ingredient_id \
            WHERE r.recipe_id=?'
    rows = cur.execute(query, recipe_id).fetchall()
    return rows


def get_recipe_ingredients_with_ids(recipe_id):
    con = sqlite3.connect('model/database.db')
    cur = con.cursor()
    query = 'SELECT i.ingredient_id, i.name, q.amount, q.measurement, i.note \
            FROM recipe r \
            JOIN quantity q ON r.recipe_id=q.recipe_id \
            JOIN ingredient i ON i.ingredient_id = q.ingredient_id \
            WHERE r.recipe_id=?'
    rows = cur.execute(query, recipe_id).fetchall()
    return rows