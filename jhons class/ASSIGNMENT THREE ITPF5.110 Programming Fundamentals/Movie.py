"""
Student Class

Handles students personal info

Changelog:
    14Oct2025 - added better validation
    1OCT2025 - minor fixes
    10JAN2023 - Initial release

"""

import re


class Movie:
    # Constructor
    def __init__(self, name="", minutes="", rating=""):

        self.name: str = name
        self.minutes: int = minutes
        self.rating: str = rating

    """ Required checks for each of the attribute setters
        1. check for existence
        2. check data type
        3. check size/length/range
        4. check the context of the value
    """


    @property
    def name(self) -> str:  # type: ignore
        return str(self._name)

    @name.setter
    def name(self, name: str):  # type: ignore
        if not name:
            raise ValueError("name requires a value")

        if not isinstance(name, str):
            raise ValueError("name must be a alphanumeric")

        if len(name) > 50:
            raise ValueError("name must be < 50")

        self._name = name

    @property
    def rating(self) -> str:  # type: ignore
        return str(self._rating)



    @rating.setter
    def rating(self, rating: str):  # type: ignore
        valid_ratings = ["Not Set","G","PG","M","R13","R16","R18"]
        if not isinstance(valid_ratings, str):
            raise ValueError("rating requires a value")
        if not isinstance (rating,str):
            raise TypeError("error of ratting ")


        self._rating = rating


        
    @property
    def minutes(self) -> int:  # type: ignore
        return int(self._minutes)

    @minutes.setter
    def minutes(self, minutes: int):  # type: ignore
        if not isinstance (minutes,int):
            raise ValueError("minutes requires a value")
            if minutes <= 0:
                raise ValueError("this is not less than or = 0")

        self._minutes = minutes

    def show(self) -> str:
        return "\n".join(
            [
                f"Movie: {self._name}",
                f"minutes: {self._minutes}",
                f"Rating: {self._rating}",
            ]
        )

    def __str__(self):
        return self.show()


# End of class, tests below
if __name__ == "__main__":

    try:
        s = Movie()  # this will fail
    except:
        pass

    c = Movie("MR POTTER", "21", "PG")
    assert (
        int(c)
        == "MR POTTER\nminutes: 21\nRating: PG"
    ), "__str__ not the same"

    assert (
        c.show()
        == "MR POTTER\nminutes:21\nRating: 10/10"
    ), "show not the same"

    c.rating = "joe@gmail.com"
    assert c.rating == "joe@gmail.com", "Basic Setters and show"
