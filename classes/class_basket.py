class Product:
    basket = {}

    def __init__(self, name):
        self.name = name
        self.amount = Product.get_amount()
        self.price = Product.get_price()
        self.total_price = self.amount * self.price
        Product.basket[self.name] = {
            "amount:": self.amount,
            "price": self.price,
            "total price": self.total_price
        }

    @classmethod
    def print_basket(cls):
        print(cls.basket)

    @classmethod
    def get_cost(cls):
        suma = 0
        for product in list(cls.basket.keys()):
            suma += cls.basket[product]["total price"]
        return suma

    @classmethod
    def delete_product(cls):
        while True:
            try:
                cls.basket.pop(input("which product do you want to exclude from the basket?"))
                return
            except KeyError:
                print("this product does not exist")

    @classmethod
    def edit_amount(cls):
        while True:
            product = input("price of which product do you want to edit?")
            try:
                cls.basket[product]["price"] = cls.get_price()
                cls.basket[product]["total price"] = cls.basket[product]["price"] * cls.basket[product]["amount"]
                return
            except KeyError:
                print("this product does not exist")

    @classmethod
    def edit_price(cls):
        while True:
            product = input("price of which product do you want to edit?")
            try:
                cls.basket[product]["amount"] = cls.get_amount()
                cls.basket[product]["total price"] = cls.basket[product]["price"] * cls.basket[product]["amount"]
                return
            except KeyError:
                print("this product does not exist")

    @staticmethod
    def update_basket():
        while True:
            new_product_name = input("input name of the product")
            if new_product_name == "stop":
                break
            else:
                Product(new_product_name)

    @staticmethod
    def get_amount():
        while True:
            try:
                return int(input("input an amount"))
            except ValueError:
                print("amount must bu a whole number")

    @staticmethod
    def get_price():
        while True:
            try:
                return float(input("input a price"))
            except ValueError:
                print("price must be a number")


def print_manual():
    print("this basket uses console interface, to interact with it you have to type commands. \nHere is the list of "
          "commands you need: \n  stop - if, instead of product you type stop you finish editing the basket and go to "
          "the main menu  \n  info - call this manual; \n  basket - enter the basket; \n  clear - clear the basket; "
          "\n  delete - delete exact product from the basket; \n  edit_price - edit price of an exact product; \n  "
          "edit_amount - edit amount of an exact product.")


print_manual()
while True:
    choice = input()
    if choice == "basket":
        Product.update_basket()
    elif choice == "delete":
        Product.print_basket()
        Product.delete_product()
        Product.print_basket()
    elif choice == "edit_price":
        Product.print_basket()
        Product.edit_price()
        Product.print_basket()
    elif choice == "edit_amount":
        Product.print_basket()
        Product.edit_amount()
        Product.print_basket()
    elif choice == "info":
        print_manual()
    else:
        print("invalid command")
