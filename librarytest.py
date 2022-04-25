import unittest
from Library import *


ON_SHELF = "ON_SHELF"
ON_HOLD_SHELF = "ON_HOLD_SHELF"
CHECKED_OUT = "CHECKED_OUT"


class LibrarySimulatorTestCases(unittest.TestCase):
    def test_library_object(self):
        b1 = Book("345", "Phantom Tollbooth", "Juster")
        a1 = Album("456", "...And His Orchestra", "The Fastbacks")
        m1 = Movie("567", "Laputa", "Miyazaki")
        self.assertEqual(b1.get_author(), "Juster")
        self.assertEqual(a1.get_artist(), "The Fastbacks")
        self.assertEqual(m1.get_director(), "Miyazaki")

        self.assertEqual(b1.get_check_out_length(), 21)
        self.assertEqual(a1.get_check_out_length(), 14)
        self.assertEqual(m1.get_check_out_length(), 7)

    def test_patron_object(self):
        p1 = Patron("abc", "Felicity")
        p2 = Patron("bcd", "Waldo")
        p1.amend_fine(150)
        p2.amend_fine(-60)
        p2.amend_fine(20)
        self.assertEqual(p1.get_fine_amount(), 150)
        self.assertEqual(p2.get_fine_amount(), -40)

    def test_check_out_library_item(self):
        b1 = Book("345", "Phantom Tollbooth", "Juster")
        a1 = Album("456", "...And His Orchestra", "The Fastbacks")

        p1 = Patron("abc", "Felicity")
        p2 = Patron("bcd", "Waldo")

        lib = Library()
        lib.add_library_item(b1)
        lib.add_library_item(a1)
        lib.add_patron(p1)
        lib.add_patron(p2)

        self.assertEqual(lib.check_out_library_item("bcde", "456"), "patron not found")
        self.assertEqual(lib.check_out_library_item("bcd", "4567"), "item not found")
        self.assertEqual(a1.get_location(), ON_SHELF)
        self.assertEqual(lib.check_out_library_item("bcd", "456"), "check out successful")
        self.assertEqual(a1.get_location(), CHECKED_OUT)

    def test_request_library_item(self):
        b1 = Book("345", "Phantom Tollbooth", "Juster")
        a1 = Album("456", "...And His Orchestra", "The Fastbacks")
        m1 = Movie("567", "Laputa", "Miyazaki")

        p1 = Patron("abc", "Felicity")
        p2 = Patron("bcd", "Waldo")
        p3 = Patron("efg", "Barney")

        lib = Library()
        lib.add_library_item(b1)
        lib.add_library_item(a1)
        lib.add_patron(p1)
        lib.add_patron(p2)

        self.assertEqual(lib.request_library_item("hij", "345"), "patron not found")
        self.assertEqual(lib.request_library_item("abc", "123"), "item not found")
        self.assertEqual(b1.get_location(), ON_SHELF)
        self.assertEqual(lib.request_library_item("abc", "345"), "request successful")
        self.assertEqual(b1.get_location(), ON_HOLD_SHELF)
        self.assertEqual(lib.request_library_item("bcd", "345"), "item already on hold")

    def test_return_library_item(self):
        b1 = Book("345", "Phantom Tollbooth", "Juster")
        a1 = Album("456", "...And His Orchestra", "The Fastbacks")
        m1 = Movie("567", "Laputa", "Miyazaki")

        p1 = Patron("abc", "Felicity")
        p2 = Patron("bcd", "Waldo")

        lib = Library()
        lib.add_library_item(b1)
        lib.add_library_item(a1)
        lib.add_patron(p1)
        lib.add_patron(p2)

        lib.check_out_library_item("bcd", "456")
        self.assertEqual(lib.return_library_item("567"), "item not found")
        self.assertEqual(lib.return_library_item("345"), "item already in library")
        self.assertEqual(lib.return_library_item("456"), "return successful")
        self.assertEqual(a1.get_location(), "ON_SHELF")


if __name__ == '__main__':
    unittest.main()
