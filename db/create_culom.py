import sqlite3
from db.read_db import read_db


def add_coulmnb_type1(name,type1):

    conn = sqlite3.connect("../sibolt.db")
    cur = conn.cursor()
    solider = read_db(f"alter table soldier add COLUMN {name} {type1}")

    conn.commit()
    conn.close()




add_coulmnb_type1("Where1","text")