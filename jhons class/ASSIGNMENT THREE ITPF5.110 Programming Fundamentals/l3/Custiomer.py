"""
Student Class

Handles students personal info

Changelog:
    14Oct2025 - added better validation
    1OCT2025 - minor fixes
    10JAN2023 - Initial release

"""

import re

#-------------------Custiomer class------------------#
class custiomer:
    # Constructor
    def __init__(self, name="", contact="", email=""):

        self.name: str = name
        self.contact: str = contact
        self.email: str = email

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
    def email(self) -> str:  # type: ignore
        return str(self._email)

    @email.setter
    def email(self, email: str):  # type: ignore

        # 1. check for existence
        if not email:
            raise ValueError("email requires a value")

        # 2. check data type
        if not isinstance(email, str):
            raise ValueError("email must be a alphanumeric")

        # 3. check size/length/range
        if len(email) > 100:
            raise ValueError("email must be < 100")

        # 4. check the context of the value
        # https://regexr.com/
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

        if not (re.fullmatch(regex, email)):
            raise ValueError("email format is invalid")

        self._email = email

    @property
    def contact(self) -> str:  # type: ignore
        return str(self._contact)

    @contact.setter
    def contact(self, contact: str):  # type: ignore
        if not contact:
            raise ValueError("contact requires a value")
        self._contact = contact

    def show(self) -> str:
        return "\n".join(
            [
                f"Customer: {self._name}",
                f"Contact: {self._contact}",
                f"Email: {self._email}",
            ]
        )

    def __str__(self):
        return self.show()


# End of class, tests below
if __name__ == "__main__":

    try:
        s = custiomer()  # this will fail
    except:
        pass

    c = custiomer("Joe Bloggs", "021-123-1234", "joe.bloggs@mail.com")
    assert (
        str(c)
        == "Joe Bloggs\nContact: 021-123-1234\nEmail: joe.bloggs@mail.com"
    ), "__str__ not the same"

    assert (
        c.show()
        == "Joe Bloggs\nContact: 021-123-1234\nEmail: joe.bloggs@mail.com"
    ), "show not the same"

    c.email = "joe@gmail.com"
    assert c.email == "joe@gmail.com", "Basic Setters and show"