"""
bookings class Class

Handles booking  info


"""

import re

#---------------Customer class---------------#
class customer:
    def __init__(self, name, contact, email):
        self._name = name
        self._contact = contact
        self._email = email

        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value
            raise ValueError("name is required a value")
        if not isinstance(value, str):
            raise ValueError("name is required a value")
        self._name = value.strip()

#---------------Sesion ------------#
    def __init__(self):
        self._session = session
    
    @property
    def session(self):
        return self._sesion

    @session.setter
    def session(self, session):
        if not value
            raise ValueError("please pick the proper sesion")
        if not isinstance(value, str):
            raise ValueError("is not the value sorry")
        self._session = value.strip
#----------------movie ------------#

    def __init__(self, title):
        self._title: str = title

    def __str__(self):
        return self.title
    
    @property
    def movie(self):
        return self._movie

    @movie.setter
    def movie(self,movie)
#-------------seats -----------------#

    def __init__(self):
        self.seats: str = seats
    
    @property
    def seats(self):
        return self._seats
    
    @seats.setter
    def seats(self,seats)
#--------------------Class --------------#

    # Constructor
    def __init__(self, customer="", session="", movie="", seats=""):

        self.customer: str = customer
        self.session: str = session
        self.movie: str = movie
        self.seats: int = seats

    def makeBookings(self):
        if not isinstance(self.custiomer, Customer)
            raise ValueError ("must be in customer object!!")#main check
        if self.session == "not set" or not self.movie:
            raise ValueError("booking must have movi sesion")
        return self

    def show(self):
        return f"Bookings for {self.custiomer.name}"
#---------------edit / remove boooking sections--------#


#-----------------Tests-------------------#
cust = Customer(name="Joe Bloggs", contact="021-123-1234", email="joe.bloggs@mail.com")

# Create a booking using the customer object
booking = Booking(customer=cust, session="7PM Friday", movie="Inception", seats=2)
booking.makeBooking()

# Show booking details
print(booking.show())
