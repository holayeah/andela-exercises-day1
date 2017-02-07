class Car:
    def __init__(self, name='General', model='GM', car_type=None):
        self.name = name
        self.model = model
        self.speed = 0

        # setting number of doors, 
        self.num_of_doors = 4
        if name == 'Porshe' or name == 'Koenigsegg':
            self.num_of_doors = 2

        # setting the number of wheels
        self.num_of_wheels = 4
        if car_type == 'trailer':
            self.num_of_wheels = 8

        # setting car type
        if not car_type:
            car_type = 'saloon'

        self.type = car_type
 

    def is_saloon(self):
        if self.type == 'saloon':
            return True
        return False

    def drive(self, speed=None):
        if speed:
            if self.type == 'trailer':
                self.speed = speed * 11
            else:
                self.speed = 10 ** speed
        return self
