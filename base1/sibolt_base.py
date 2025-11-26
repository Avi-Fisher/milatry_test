from base1.class_base.base2 import Base
from base1.living_house.basic_house import *
from base1.living_house.room import Room


def create_sibolot():

    sibolot = Base("sibolot","sibolt","sibol")


    for j in range(2):
        sibolot.add_house(House(j,80))

        for i in range(10):
            sibolot.house[j].add_room(Room(8))

    return sibolot

