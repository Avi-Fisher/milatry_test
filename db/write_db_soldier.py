import sqlite3
import csv


def write_db(csv):
    conn = sqlite3.connect("sibolt.db")
    cur =conn.cursor()
    cur.execute("CREATE TABLE soldier (num_id integer primary key, first_name text, lest_name text, gender text, city text, distans integer);")



    for i in csv:

        cur.execute(f"INSERT INTO soldier (num_id, first_name, lest_name, gender, city, distans) VALUES (?, ?, ?, ?, ?, ?);", (int(i["מספר אישי"]), i["שם פרטי"], i["שם משפחה"], i["מין"], i["עיר מגורים"], int(i["מרחק מהבסיס"])))
        conn.commit()

    conn.close()



