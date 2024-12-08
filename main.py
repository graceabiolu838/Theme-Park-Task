class Attraction:
    def __init__(self, name, capacity):
        self._name = name
        self._capacity = capacity
    def get_details(self, name, capacity):
        return f"Attraction: {self._name}, Capacity: {self._capacity}\n"
    def start(self):
        return f"The attraction is starting\n"

class ThrillRide(Attraction):
    def __init__(self, name, capacity, min_hgt):
        super().__init__(name, capacity)
        self._min_hgt = min_hgt
    def start(self):
        return f"Thrill Ride {self._name} is now starting. Hold on tight!\n"
    def is_eligible(self, height):
        return False if height<self._min_hgt else True

class FamilyRide(Attraction):
    def __init__(self, name, capacity, min_age):
        super().__init__(name, capacity)
        self._min_age = min_age
    def start(self):
        return f"Family Ride {self._name} is now starting. Enjoy the fun!"
    def is_eligible(self, age):
        return False if age<self._min_age else True

class Staff:
    def __init__(self, name, role):
        self._name = name
        self._role = role
    def work(self):
        return f"Staff {self._name} is performing their role.\n"

class Visitor:
    def __init__(self, name, age, height):
        self._name = name
        self._age = age
        self._height = height
    def ride(self, attraction):
        #https://betterstack.com/community/questions/how-to-get-class-name-of-instance-in-python/
        #https://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance
        instance = type(attraction).__name__
        if instance=="ThrillRide":
            if attraction.is_eligible(self._height): 
                print(attraction.start())
            else: print(f"{self._name} is too short:(\n")
        else:
            if attraction.is_eligible(self._age):
                print(attraction.start())
            else:
                print(f"{self._name} is A MINORRRRR\n")
    
grace = Visitor("Grace", 4, 180)
ride1 = ThrillRide("Taste of Hell", 20, 170) #this and below are the attractions
#passed into the Visitor.ride(self, attraction)
ride2 = FamilyRide("Diddy's Paradise", 30, 4)
grace.ride(ride1)
grace.ride(ride2)
