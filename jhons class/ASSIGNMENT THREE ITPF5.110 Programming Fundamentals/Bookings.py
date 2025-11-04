"""
bookings class Class

Handles booking  info


"""

import re

#---------------Bookings class---------------#
class Bookings:
    def __init__(self, bookingid, date, customer, session, seats, movie, time):
        self._bookingid = bookingid
        self._date = date
        self._customer = customer
        self._session = session
        self._seats = seats
        self._movie = movie
        self._time = time


#-----------Booking id Propoty----------------#
    @property
    def bookingid(self) -> str:
        return str(self._bookingid)

#----------- Date Propoty-----------------#\
    @property
    def date(self):
        return self.date

    @date.setter
    def date(self, dateofbooking: date):
        if not isinstance(dateofbooking, str):
            raise ValueError("must use numbers")
        self._date = dateofbooking
#---------------Sesion propoty------------#

    @property
    def session(self) -> str:
        return str(self._session)

    @session.setter
    def session(self, session: str):
        if not session:
            raise ValueError("please pick the proper sesion")
        
        if not isinstance(session, str):
            raise ValueError("is not the value sorry")
        
        self._session = session
#----------------movie ------------#
    
    @property
    def movie(self) -> str:
        return str(self._movie)

    @movie.setter
    def movie(self, movie: str):
        if not isinstance(movie, str):
            raise ValueError("please pick one of the valid movies")
        self._movie = movie
#-------------seats -----------------#
    @property
    def seats(self):
        return int(self._seats)
    
    @seats.setter
    def seats(self,seats: int):
        if not isinstance(seats, int):
            raise ValueError("please pick one of the availible seats")
        self._seats = seats
#--------------------method makebookings --------------#

    def makeBookings(self):
        if self._customer and self._movie and self._session != "not set":
            self._bookingid = f"{self._session}~~{self._email}"


#---------------edit / remove boooking sections--------#

    def editBookings(self, date = None, customer = None, session = None, seats = None, movie = None, time = None):
        if customer:
            self._customer = customer
        if date:
            self._date = date
        if session:
            self._session = session
        if seats:
            self._seats = seats
        if movie:
            self._movie = movie
        if time:
            self._time = time
    
        

#-------------Remove bookings----------------------#
    def removeBookings(self, value: str):
        if not value: #check for valid booking
            raise ValueError
        for i in range(len(self.booking)):
            if self._booking[i].code == value:
                del self._booking[i]
                break
        




    def show(self):
        return f"Bookings for {self.custiomer.name}"
#-----------------Tests-------------------#
# End of class, tests below
if __name__ == "__main__":

    try:
        b = Bookings()  # this will fail
    except:
        pass

    b = Bookings("MR POTTER", "21", "PG")
    assert (
        int(b)
        == "MR POTTER\nminutes: 21\nRating: PG"
    ), "__str__ not the same"

    assert (
        b.show()
        == "MR POTTER\nminutes:21\nRating: 10/10"
    ), "show not the same"

    b.rating = "joe@gmail.com"
    assert b.rating == "joe@gmail.com", "Basic Setters and show"