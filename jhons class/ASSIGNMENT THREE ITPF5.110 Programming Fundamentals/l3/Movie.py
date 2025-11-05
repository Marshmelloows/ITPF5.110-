"""
Student Class

Handles students personal info

Changelog:
    14Oct2025 - added better validation
    1OCT2025 - minor fixes
    10JAN2023 - Initial release

"""

import re

#----------------<Movie~~Class>---------------#

class Movie:
    # Constructor
    def __init__(self, name="", minutes="", rating=""):

        self.name = name
        self.minutes = minutes
        self.rating = rating

    """ Required checks for each of the attribute setters
        1. check for existence
        2. check data type
        3. check size/length/range
        4. check the context of the value
    """

#---------------------<Name>----------------#
    @property
    def name(self) -> str:  # type: ignore
        return self._name

    @name.setter    
    def name(self, name: str):  # type: ignore
        if not name:
            raise ValueError("name requires a value")

        if not isinstance(name, str):
            raise TypeError("name must be a alphanumeric")

        if len(name) > 50:
            raise ValueError("name must be < 50")

        self._name = name
#----------------------<Rating>----------------#
    @property
    def rating(self) -> str:  # type: ignore
        return self._rating

    @rating.setter
    def rating(self, rating: str):  # type: ignore
        valid_ratings = ["Not Set", "G", "PG", "M", "R13" ,"R16" ,"R18" ]
        if not rating:
            raise ValueError("rating requires a value")
        if not isinstance(rating, str):
            raise TypeError("Rating must be a string")
        if rating not in valid_ratings:
            raise ValueError(f"Rating must be of {valid_ratings}")


        self._rating = rating

#---------------------<Minutes>------------------#

    @property
    def minutes(self) -> int:  # type: ignore
        return self._minutes

    @minutes.setter
    def minutes(self, minutes: int):  # type: ignore
        if not isinstance (minutes,str):
            minutes = int(minutes)
        
        if not isinstance (minutes,int):
            raise TypeError("minits as intager")
        
        if minutes <= 0:
            raise ValueError("this is not less than or = 0")

        self._minutes = minutes
#---------------<Show>---------------#
    def show(self) -> str:
        return "\n".join(
            [
                f"Movie: {self.name}",
                f"minutes: {self.minutes}",
                f"Rating: {self.rating}",
            ]
        )

    def __str__(self):
        return self.show()


# End of class, tests below
if __name__ == "__main__":

    try:
        m = Movie()  # this will fail
    except:
        pass

    m = Movie("MR POTTER", 21, "PG")

    assert (

        str(m)
        == "Movie: MR POTTER\nminutes: 21\nRating: PG"
    ), "__str__ not the same"

    assert (
        m.show()
        == "Movie: MR POTTER\nminutes: 21\nRating: PG"
    ), "show not the same"

    m.rating = "PG"
    assert m.rating == "PG", "Basic Setters and show"
