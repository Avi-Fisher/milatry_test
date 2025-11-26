import sqlite3


def updata_solider(solder):

    conn = sqlite3.connect("../sibolt.db")
    cur = conn.cursor()



    cur.execute(f"update soldier set 'Where1' = {solder["placement"]} where num_id = {solder["num_id"]}")
    try:
        cur.execute(f"update soldier set 'Where1' = {solder["place"]} where num_id = {solder["num_id"]}")
    except:
        pass

    conn.commit()
    conn.close()

