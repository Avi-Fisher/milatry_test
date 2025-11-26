
class Soldier():

    def __init__(self,id_num,first_name,last_name,gender,city,distans):

        self._id_num = id_num
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.city = city
        self.distans = distans
        self.placement = False


    @property
    def get_id_num(self):

        return self._id_num














