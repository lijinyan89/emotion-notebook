import sqlite3 as lite
import time

def rebuild_db():
    con = lite.connect('notebook.db')
    with con:
        cur = con.cursor()
        cur.execute("DROP table if exists emotion_notebook")
        cur.execute("""CREATE table emotion_notebook
                        (name text, dt text, note text)""")
    print("数据路已更新！")

def insert_data(name, dt, note):
    con = lite.connect('notebook.db')
    with con:
        cur = con.cursor()
        cur.execute("INSERT into emotion_notebook values(?,?,?)", (name, dt, note))

def obtain_data(name):
    con = lite.connect('notebook.db')
    with con:
        cur = con.cursor()
        cur.execute('SELECT name, dt, note from emotion_notebook where name=:name',
                    {"name" : name})
        row = cur.fetchone()
        weather_str = "{}   {}, {}".format(row[0], row[1], row[2])
        return weather_str

def get_history():
    con = lite.connect('notebook.db')
    with con:
        cur = con.cursor()
        cur.execute('SELECT * from emotion_notebook')
        rows = cur.fetchall()
    return rows


def update(name, note):
    con = lite.connect('notebook.db')
    with con:
        cur = con.cursor()
        cur.execute('UPDATE emotion_notebook set note=? where name=?', (note, name))
if __name__ == "__main__":
    while True:
        rebuild_db()
        time.sleep(3 * 24 * 60 * 60)
