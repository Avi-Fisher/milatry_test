from db.up_data_sodier import updata_solider

class Base():

    def __init__(self,name,comandor, place):

        self.name = name
        self.comandor = comandor
        self.place = place
        self.soldier = []
        self.house = []
        self.house_bed_empty = []
        self.soldier_sleep_home = []
        self.soldier_sleep_base = []

    def add_soldier(self,soldier):


        self.soldier.append(soldier)



    def add_house(self,house):

        self.house.append(house)
        self.house_bed_empty.append(True)


    def add_bed_to_soldier(self,solder):

        for i,house in enumerate(self.house):

            if house.bed_free:
                stile_free = house.add_soldier(solder)

                self.soldier_sleep_base.append(solder)

                self.house_bed_empty.pop(i)
                self.house_bed_empty.insert(0,stile_free)

                solder["placement"] = True
                solder["place"] = {"house": i}



            else:
                self.house_bed_empty.pop(i)
                self.house_bed_empty.insert(0,False)

            self.soldier_sleep_home.append(solder)
            solder["placement"] = False
            solder["place"] = "whiting in the list"

            updata_solider(solder)






    def orgniz_bed_base(self):

        for s in self.soldier:

            self.add_bed_to_soldier(s)



















