import sqlite3


def read_db(name):
    conn = sqlite3.connect("../sibolt.db")
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()

    cur.execute(name)
    soldier = [dict(row) for row in cur.fetchall()]

    conn.close()

    return soldier



