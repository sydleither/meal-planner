import sqlite3


def add_planner_to_database(planner):
    con = sqlite3.connect('model/database.db')
    cur = con.cursor()
    
    for meal in planner:
        cur.execute('INSERT INTO planner VALUES (NULL,?,?,?,?,?,?,?,?)', \
                    (meal.meal, meal.monday, meal.tuesday, meal.wednesday, \
                     meal.thursday, meal.friday, meal.saturday, meal.sunday))
    
    con.commit()
    con.close()
    
    
def clear_planner():
    con = sqlite3.connect('model/database.db')
    cur = con.cursor()
    cur.execute('DELETE FROM planner;')
    con.commit()
    cur.execute('VACUUM;')
    con.commit()
    con.close()
    
    
def get_planner():
    con = sqlite3.connect('model/database.db')
    cur = con.cursor()
    query = 'SELECT meal,monday,tuesday,wednesday,thursday,friday,saturday,sunday FROM planner'
    rows = cur.execute(query).fetchall()
    return rows