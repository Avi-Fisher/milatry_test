from base1.soldier.create_soldier import Soldier
from base1.class_base.base2 import Base


def get_csv_soldier(csv):

    sibolt = Base("sibolt", "siboli", "sibolot")

    for s in csv:
        soldier = Soldier(s["מספר אישי"],s["שם פרטי"], s["שם משפחה"], s["מין"], s["עיר מגורים"], s["מרחק מהבסיס"])
        sibolt.add_soldier(soldier)

