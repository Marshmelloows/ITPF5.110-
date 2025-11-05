#Cinima class

import Movie
import Bookings
import Custiomer

#-------------------<Class~~Cinema>------------#

class Cinema:
    #Constructor
    def __init__(self, movies, bookings, custiomer):
        self._movies = movies #list of movies
        self._bookings: list = bookings #list of bookings
        self._Custiomer: list = custiomer #list of custiomers



#--------------<ADD() MOVIES>-----------#
#    def add(self):
       # if self._movies
#-------------<Get~Movie~Names()>---------#

#-------------<Remove>-----------#
    def remove(self, movie: str):
        if not movie:#Checks for valid movie
            raise ValueError("must give the name of the movie")
        for i in range(len(self._movies)):
            if self._movies[i].code == movie:
                del self._movies[i]
            break
            
        self._movies

#-------------<Find~Movie~Items>-------------#

#-------------<Find~Rated~Movie~Names>------------#

#-------------<Get~Total~Minutes>-------------#


        

