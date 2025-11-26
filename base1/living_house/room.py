

class Room():

    def __init__(self,num_bed):

        self.num_bed = num_bed
        self.list_soldier = []
        self.bed_clear = True


    def add_soldier(self,soldier):

        if self.bed_clear:
            self.list_soldier.append(soldier)

            soldier["place"] = {"bed": len(self.list_soldier)}

            if len(self.list_soldier) == self.num_bed:
                self.bed_clear = False
            return False

        return True


    def remove_soldier(self,id):

        for s in self.list_soldier:
            if s["num_id"] == id:
                self.list_soldier.remove(s)

        self.bed_clear = True

