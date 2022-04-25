# Author: Matthew Armstrong
# Date: 10/06/2021
# Description: library simulator involving multiple classes -- library item, patron, library.
# this project demonstrates inheritance by the book, album, and movie sub classes.


class LibraryItem:
    """represents library class"""
    def __init__(self, library_item_id, title):
        """initializes library item id, and title"""
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = None

    def get_library_item_id(self):
        """returns the library item id"""
        return self._library_item_id

    def get_title(self):
        """returns the item title"""
        return self._title

    def set_location(self, location):
        """sets location of library items"""
        self._location = location

    def get_location(self):
        """returns item location"""
        return self._location

    def get_checked_out_by(self):
        """returns who checked out the item"""
        return self._checked_out_by

    def set_checked_out_by(self, patron):
        """sets who checked out the item."""
        self._checked_out_by = patron

    def get_requested_by(self):
        """returns who requested the item"""
        return self._requested_by

    def set_requested_by(self, patron):
        """sets who requested the item"""
        self._requested_by = patron

    def get_date_checked_out(self):
        """returns the check out date"""
        return self._date_checked_out

    def set_date_checked_out(self, date):
        """retrieves the check out date"""
        self._date_checked_out = date


class Book(LibraryItem):
    """represents a book
    inherits from LibraryItem"""
    def __init__(self, library_item_id, title, author):
        super().__init__(library_item_id, title)
        self._author = author
        self._check_out_length = 21

    def get_author(self):
        """returns author"""
        return self._author

    def get_check_out_length(self):
        """returns length of time item can be checked out"""
        return self._check_out_length


class Album(LibraryItem):
    """represents an album
    inherits from LibraryItem"""
    def __init__(self, library_item_id, title, artist):
        super().__init__(library_item_id, title)
        self._artist = artist
        self._check_out_length = 14

    def get_artist(self):
        """returns artist"""
        return self._artist

    def get_check_out_length(self):
        """returns length of time item can be checked out"""
        return self._check_out_length


class Movie(LibraryItem):
    """represents a movie
    inherits from LibraryItem"""
    def __init__(self, library_item_id, title, director):
        super().__init__(library_item_id, title)
        self._director = director
        self._check_out_length = 7

    def get_director(self):
        """returns director"""
        return self._director

    def get_check_out_length(self):
        """returns length of time item can be checked out"""
        return self._check_out_length


class Patron:
    """represents the library patron"""
    def __init__(self, patron_id, name):
        """initializes patron id and name properties"""
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0.00

    def get_patron_id(self):
        """gets the patron id"""
        return self._patron_id

    def get_name(self):
        """gets the patron name"""
        return self._name

    def get_checked_out_items(self):
        """gets the items checked out by the patron"""
        return self._checked_out_items

    def get_fine_amount(self):
        """gets the fine amount the patron is due"""
        return self._fine_amount

    def set_fine_amount(self, fine):
        """sets the fine amount due"""
        self._fine_amount = fine

    def add_library_item(self, library_item):
        """adds the library item"""
        return self._checked_out_items.append(library_item)

    def remove_library_item(self, library_item):
        """removes the library item"""
        return self._checked_out_items.remove(library_item)

    def amend_fine(self, fine_amount):
        """amends the library fine"""
        self._fine_amount += fine_amount


class Library:
    def __init__(self):
        """initializes the library properties"""
        self._holdings = []
        self._members = []
        self._current_date = 0

    def get_holdings(self):
        """gets items in the library"""
        return self.get_holdings()

    def get_members(self):
        """gets library patrons"""
        return self.get_members()

    def get_current_date(self):
        """returns the current date"""
        return self._current_date

    def set_current_date(self, date):
        """sets the current date"""
        self._current_date = date

    def add_library_item(self, item):
        """adds library item"""
        return self._holdings.append(item)

    def add_patron(self, patron):
        """adds patron"""
        return self._members.append(patron)

    def lookup_library_item_from_id(self, item_id):
        """looks up library item from id, otherwise returns none"""
        for item in self._holdings:
            if LibraryItem.get_library_item_id(item) == item_id:
                return item
        return None

    def lookup_patron_from_id(self, patron_id):
        """looks up patron member from id, otherwise returns none"""
        for patron in self._members:
            if Patron.get_patron_id(patron) == patron_id:
                return patron
        return None

    def check_out_library_item(self, patron_id, library_item_id):
        """checks out library item"""
        patron = self.lookup_patron_from_id(patron_id)
        check_out_item = self.lookup_library_item_from_id(library_item_id)

        if patron is None:
            return "patron not found"
        if check_out_item is None:
            return "item not found"
        if check_out_item.get_location() == "CHECKED_OUT":
            return "item already checked out"
        if check_out_item.get_requested_by() is not None:
            return "item on hold by other patron"
        else:
            check_out_item.set_checked_out_by(patron)
            check_out_item.set_date_checked_out(self.get_current_date())
            check_out_item.set_location("CHECKED_OUT")

            if check_out_item.get_requested_by() == patron:
                check_out_item.set_requested_by(None)
            patron.add_library_item(check_out_item)
        return "check out successful"

    def return_library_item(self, library_item_id):
        """returns library item"""
        return_item = self.lookup_library_item_from_id(library_item_id)

        if return_item is None:
            return "item not found"
        if return_item.get_location() != "CHECKED_OUT":
            return "item already in library"

        patron = return_item.get_checked_out_by()
        patron.remove_library_item(return_item)

        if return_item.get_requested_by() is None:
            return_item.set_location("ON_SHELF")
        else:
            return_item.set_location("ON_HOLD_SHELF")

        return_item.set_checked_out_by(None)
        return "return successful"

    def request_library_item(self, patron_id, library_item_id):
        """requests library item"""
        patron = self.lookup_patron_from_id(patron_id)
        requested_item = self.lookup_library_item_from_id(library_item_id)

        if patron is None:
            return "patron not found"

        if requested_item is None:
            return "item not found"
        if requested_item.get_location() == "ON_HOLD_SHELF":
            return "item already on hold"

        requested_item.set_requested_by(patron)

        if requested_item.get_location() == "ON_SHELF":
            requested_item.set_location("ON_HOLD_SHELF")
            return "request successful"

    def pay_fine(self, patron_id, dollars):
        """payment for late fees"""
        patron = self.lookup_patron_from_id(patron_id)
        if patron is None:
            return "patron not found"
        else:
            patron.amend_fine(-dollars)
            return "payment successful"

    def increment_current_date(self):
        """increase the payment fines by 10 cents"""
        self._current_date += 1
        for patron in self._members:
            for item in patron.get_checked_out_items():
                if self._current_date - item.get_date_checked_out() > item.get_check_out_length():
                    fine_amount = 0.10
                    patron.amend_fine(fine_amount)


if __name__ == "__main__":
    b1 = Book("345", "Phantom Tollbooth", "Juster")
    a1 = Album("456", "...And His Orchestra", "The Fastbacks")
    m1 = Movie("567", "Laputa", "Miyazaki")
    print(b1.get_author())
    print(a1.get_artist())
    print(m1.get_director())

    p1 = Patron("abc", "Felicity")
    p2 = Patron("bcd", "Waldo")

    lib = Library()
    lib.add_library_item(b1)
    lib.add_library_item(a1)
    lib.add_patron(p1)
    lib.add_patron(p2)

    lib.check_out_library_item("bcd", "456")
    loc = a1.get_location()
    lib.request_library_item("abc", "456")
    for i in range(57):
        lib.increment_current_date()  # 57 days pass
    p2_fine = p2.get_fine_amount()
    lib.pay_fine("bcd", p2_fine)
    lib.return_library_item("456")
