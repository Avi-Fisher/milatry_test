import abc
from tkinter.font import names


class House():

    def __init__(self,name,num_bed,menger = None,):

        self.name = name
        self.num_bed = num_bed
        self.menger = menger
        self.list_room = []
        self.list_empty_bed_room = []
        self.bed_free = True



    def add_room(self,room):

        self.list_room.append(room)
        self.list_empty_bed_room.append(True)


    def add_soldier(self,soldier):

        for i,room in enumerate(self.list_room):

            if room.bed_clear:
                bed = room.add_soldier(soldier)

                soldier["place"] = {"Room": i}

                self.list_empty_bed_room.pop(i)
                self.list_empty_bed_room.insert(0,bed)


        if not True in self.list_empty_bed_room:
            self.bed_free = False
            return False

        return True











