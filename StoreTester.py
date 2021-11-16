# Author: Matthew Armstrong
# Date: 10/03/2021
# Description: unit test for store.py
import unittest
from Store import Store, Product, Customer, InvalidCheckoutError


class TestStoreTester(unittest.TestCase):
    """testing the store.py"""
    def test_product(self):
        """tests the product id"""
        p1 = Product("1", "Peach", "this is a native fruit", 2.99, 2)
        self.assertEqual(p1.get_title(), "Peach")

    def test_member(self):
        """tests the customer id"""
        c2 = Customer("Isabelle", "68", True)
        self.assertNotEqual(c2.get_customer_id(), "45")

    def test_decrease_quantity(self):
        """tests decrease quantity function"""
        p1 = Product("1", "Peach", "this is a native fruit", 2.99, 10)
        p1.decrease_quantity()
        self.assertEqual(p1.get_quantity_available(), 9)

    def test_is_premium_member(self):
        """tests is_premium_member function"""
        nooks_cranny = Store()
        p1 = Product("1", "Peach", "this is a native fruit", 2.99, 1)
        nooks_cranny.add_product(p1)
        p2 = Product("2", "Apple", "this is non-native fruit", 3.99, 1)
        nooks_cranny.add_product(p2)
        p3 = Product("3", "Axe", "tool to grind with", 5.99, 2)
        nooks_cranny.add_product(p3)
        p4 = Product("4", "Shovel", "tool to dig stuff up", 6.99, 2)
        nooks_cranny.add_product(p4)

        c1 = Customer("Villager", "45", True)
        nooks_cranny.add_member(c1)
        c2 = Customer("Isabelle", "68", True)
        nooks_cranny.add_member(c2)
        c3 = Customer("KK", "6", True)
        nooks_cranny.add_member(c3)
        c4 = Customer("Redd", "9", False)
        nooks_cranny.add_member(c3)

        self.assertTrue(c1.is_premium_member())
        self.assertTrue(c2.is_premium_member())
        self.assertTrue(c3.is_premium_member())
        self.assertFalse(c4.is_premium_member())

    def test_product_search(self):
        """tests product_search function"""
        p1 = Product("1", "Peach", "this is a native fruit", 2.99, 1)
        p2 = Product("2", "Apple", "this is non-native fruit", 3.99, 1)
        p3 = Product("3", "Axe", "tool to grind with", 5.99, 2)
        p4 = Product("4", "Shovel", "tool to dig stuff up", 6.99, 2)

        nooks_cranny = Store()

        nooks_cranny.add_product(p1)
        nooks_cranny.add_product(p2)
        nooks_cranny.add_product(p3)
        nooks_cranny.add_product(p4)

        self.assertEqual(nooks_cranny.product_search("tool"), ["3", "4"])

    def test_add_product_to_member_cart(self):
        """tests add product to member cart function"""
        p1 = Product("1", "Peach", "this is a native fruit", 2.99, 1)
        p2 = Product("2", "Apple", "this is non-native fruit", 3.99, 0)
        c1 = Customer("Villager", "45", True)
        nooks_cranny = Store()
        nooks_cranny.add_member(c1)
        nooks_cranny.add_product(p1)
        nooks_cranny.add_product(p2)

        self.assertEqual(nooks_cranny.add_product_to_member_cart("1", "45"), "product added to cart")
        self.assertEqual(nooks_cranny.add_product_to_member_cart("2", "45"), "product out of stock")

    def test_check_out_member(self):
        """tests check_out_member_function"""
        p1 = Product("1", "Peach", "this is a native fruit", 2.99, 1)
        p2 = Product("2", "Apple", "this is non-native fruit", 3.99, 1)
        p3 = Product("3", "Axe", "tool to grind with", 5.99, 2)
        p4 = Product("4", "Shovel", "tool to dig stuff up", 6.99, 2)

        c1 = Customer("Villager", "45", True)

        nooks_cranny = Store()
        nooks_cranny.add_member(c1)
        nooks_cranny.add_product(p1)
        nooks_cranny.add_product(p2)
        nooks_cranny.add_product(p3)
        nooks_cranny.add_product(p4)
        nooks_cranny.add_product_to_member_cart("1", "45")
        nooks_cranny.add_product_to_member_cart("2", "45")
        nooks_cranny.add_product_to_member_cart("3", "45")
        nooks_cranny.add_product_to_member_cart("4", "45")

        self.assertAlmostEqual(nooks_cranny.check_out_member("45"), 19.96)

    def test_assert_raise_InvalidCheckoutError(self):
        """tests invalid check out error function"""
        with self.assertRaises(InvalidCheckoutError):
            p1 = Product("1", "Peach", "this is a native fruit", 2.99, 1)
            c1 = Customer("Villager", "45", False)
            nooks_cranny = Store()
            nooks_cranny.add_product(p1)
            nooks_cranny.add_member(c1)
            nooks_cranny.add_product_to_member_cart("1", "45")
            nooks_cranny.check_out_member("invalid")


if __name__ == '__main__':
    unittest.main()
