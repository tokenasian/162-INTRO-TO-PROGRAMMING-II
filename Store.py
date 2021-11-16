# Author: Matthew Armstrong
# Date: 10/03/2021
# Description: an online store stimulator containing three private classes:
# product, customer, and store.
class InvalidCheckoutError(Exception):
    """error that checks for when a customer's member id cannot be found"""
    pass


class Product:
    """represents products found in a store"""
    def __init__(self, product_id, title, description, price, quantity_available):
        """initializes five product values"""
        self._product_id = product_id
        self._title = title
        self._description = description
        self._price = price
        self._quantity_available = quantity_available

    def get_product_id(self):
        """returns product id"""
        return self._product_id

    def get_title(self):
        """returns product title"""
        return self._title

    def get_description(self):
        """returns product description"""
        return self._description

    def get_price(self):
        """returns product price"""
        return self._price

    def get_quantity_available(self):
        """returns stock available"""
        return self._quantity_available

    def decrease_quantity(self):
        """decrease stock quantity by one"""
        self._quantity_available -= 1


class Customer:
    """represents customers that shop in the store"""
    def __init__(self, name, customer_id, premium_member):
        """initializes customer values"""
        self._customer_name = name
        self._customer_id = customer_id
        self._premium_member = premium_member
        # A customer's cart is a collection of Product ID codes
        self._cart = []

    def get_name(self):
        """returns customer name"""
        return self._customer_name

    def get_customer_id(self):
        """returns customer id"""
        return self._customer_id

    def is_premium_member(self):
        """returns premium member status"""
        return self._premium_member

    def get_cart(self):
        """returns customer cart"""
        return self._cart

    def add_product_to_cart(self, product):
        """takes a product id code and adds the product to the customers cart"""
        self._cart.append(product)

    def empty_cart(self):
        """empties the customers cart"""
        self._cart.clear()


class Store:
    """represents the store"""

    def __init__(self):
        """initializes the inventory and members values"""
        self._store_inventory = []
        self._store_member = []

    def add_product(self, product):
        """adds a product to the store inventory"""
        self._store_inventory.append(product)

    def add_member(self, customer):
        """adds a customer to the store membership"""
        self._store_member.append(customer)

    def lookup_product_from_id(self, product_id):
        """returns the product with the matching id. if matching id is unavailable, returns special value none"""
        # check for valid product id
        for product in self._store_inventory:
            if product.get_product_id() == product_id:
                return product
        return None

    def lookup_member_from_id(self, customer_id):
        """returns the customer with the matching id. if matching id is unavailable, returns special value none"""
        # check for valid customer id
        for customer in self._store_member:
            if customer.get_customer_id() == customer_id:
                return customer
        return None

    def product_search(self, search_string):
        """returns sorted product ids"""
        sorted_list = []
        for product in self._store_inventory:
            if search_string.lower() in product.get_title().lower() + product.get_description().lower():
                sorted_list.append(product.get_product_id())
        sorted_list.sort()
        return sorted_list

    def add_product_to_member_cart(self, product_id, customer_id):
        """takes product id and customer id, adds product to customers cart"""
        product = self.lookup_product_from_id(product_id)
        customer = self.lookup_member_from_id(customer_id)

        if product is None:
            # check if the product id is in inventory
            return "product ID not found"
        if customer is None:
            # check if the customer is a member
            return "member ID not found"
        if product.get_quantity_available() > 0:
            # add the product to the customer cart if it is in stock
            customer.add_product_to_cart(product)
            return "product added to cart"
        else:
            # check if the product is not available
            return "product out of stock"

    def check_out_member(self, customer_id):
        """verifies if customer is a valid member adds a fee if customer is not a member, computes total"""
        customer = self.lookup_member_from_id(customer_id)
        if customer is None:
            # raise an error if member ID is not found
            raise InvalidCheckoutError()

        cart_total = 0
        for product in customer.get_cart():
            # check if product is in stock
            if product.get_quantity_available() > 0:
                # decrease stock quantity by one if product is in stock
                product.decrease_quantity()
                # add product price to cart total if product is in stock
                cart_total += product.get_price()

        if not customer.is_premium_member():
            # add non-membership fee
            cart_total *= 1.07
        # clear the shopping cart
        customer.empty_cart()
        return cart_total


def main():
    """test"""
    try:
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
        nooks_cranny.add_member(c4)

        print(nooks_cranny.product_search('fruit'))
        print(nooks_cranny.lookup_member_from_id("45").get_customer_id())
        print(nooks_cranny.add_product_to_member_cart("1", "45"))
        print(nooks_cranny.add_product_to_member_cart("2", "45"))
        print(nooks_cranny.check_out_member("45"))

        print(nooks_cranny.product_search('tool'))
        print(nooks_cranny.lookup_member_from_id("68").get_customer_id())
        print(nooks_cranny.add_product_to_member_cart("3", "68"))
        print(nooks_cranny.add_product_to_member_cart("4", "68"))
        print(nooks_cranny.check_out_member("68"))

        print(nooks_cranny.product_search('fruit'))
        print(nooks_cranny.lookup_member_from_id("6").get_customer_id())
        print(nooks_cranny.add_product_to_member_cart("1", "6"))
        print(nooks_cranny.add_product_to_member_cart("2", "6"))
        print(nooks_cranny.check_out_member("6"))

        print(nooks_cranny.product_search('tool'))
        print(nooks_cranny.lookup_member_from_id("9").get_customer_id())
        print(nooks_cranny.add_product_to_member_cart("3", "9"))
        print(nooks_cranny.add_product_to_member_cart("4", "9"))
        print(nooks_cranny.check_out_member("9"))

    except InvalidCheckoutError:
        print("Member ID not found")


if __name__ == "__main__":
    main()
