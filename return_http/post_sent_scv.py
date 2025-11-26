from db.read_db import read_db
from base1.soldier_bed import placement_from_db

def  post_sent_csv():


    sibolet = placement_from_db()

    print(sibolet)
    soldiers = read_db("select * from soldier")

    return {"soldier_sleep_home":len(sibolet.soldier_sleep_home),"soldier_sleep_base":len(sibolet.soldier_sleep_base),"solders":soldiers}


post_sent_csv()
