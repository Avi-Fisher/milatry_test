from base1.sibolt_base import create_sibolot
from db.read_db import read_db

def placement_from_db():
    sibolt = create_sibolot()
    solder = read_db("select * from soldier order by distans desc")

    print(solder)

    for s in (solder):
        sibolt.add_soldier(s)

    sibolt.orgniz_bed_base()

    return sibolt




