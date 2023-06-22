from abc import ABC ,abstractmethod
from datetime import datetime

class User(ABC):
    def __init__(self,name,email,nid):
        self.name = name
        self.email = email
#TODO : set user id dynamically
        self.__id = 0
        self.nid = nid
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError

class Rider(User):
    def __init__(self,name,email,currebt_location):
         self.current_ride = None
         self.wallet =0
         self.current_location = currebt_location
         super().__init__(name,email,nid)
    def display_profile(self):
        print(f'Rider with name : {self.name} and email:{self.email}')

    def load_cash(self,amount):
        if amount > 0:
           self.wallet +=amount

    def update_location(self,currebt_location):
        self.current_location = currebt_location
    def request_ride(self,location,destination):
        if not self.current_ride:
            #TODO: set ride properly
            #TODO:set current ride via ride match
            ride_request = None

            self.current_ride = None

class Driver(User):
    def __init__(self,name,email,nid,current_location):
        super().__init__(name,email,nid)
        self.current_location = current_location
        self.wallet = 0


    def display_profile(self):
        print(f'Driver with name : {self.name} and email : {self.email}')
    def accept_ride(self,ride):
        ride.set_driver(self)

class Ride:
    def __init__(self,started_loc,ended_loc):
        self.started_loc = started_loc
        self.ended_loc = ended_loc
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None
    def set_drive(self,drive):
        self.driver = driver
    def start_ride(self):
        self.start_time = datetime.now()
    def end_ride(self,amount):
        self.end_time = datetime.now()
        self.rider.wallet -=self.estimated_fare
        self.driver.wallet +=self.estimated_fare