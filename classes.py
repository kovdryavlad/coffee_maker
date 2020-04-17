class Ingridient:
    def __init__(self, name):
        if Ingridient.is_valid_name(name):
            self.__name = name
        else:
            self.__name = "undefined"

        self.__price = 1
    
    @property
    def price(self):
        return self.__price;

    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price;
        else:
            print("Invalid value of property 'price'")

    @property
    def name(self):
        return self.__name;

    def is_valid_name(name):
        return name != ""

    def get_info(self):
        return "{" + self.name + " | costs: " + str(self.price) +"}"

class OrderItem:
    def __init__(self, ingridient):
        self.__ingridient = ingridient
        self.__quantity = 1

    @property
    def quantity(self):
        return self.__quantity;

    @quantity.setter
    def quantity(self, quantity):
        if quantity > 0:
            self.__quantity = quantity;
        else:
            print("Invalid value of property 'quantity'")

    def get_price(self):
        return self.__ingridient.price * self.__quantity
    
    def get_info(self):
        return self.__ingridient.name + "\t\t\t" + "x" + str(self.__quantity) + "\n"

class Order:
    def __init__(self):
        self.__order_items = []

    def add_ingridient(self, ingridient, quantity):
        if ingridient in self.__order_items:
            print("Hello")
            indx = self.__order_items.index(ingridient)
            old_quantity = self.__order_items[indx].quantity
            self.__order_items[indx].quantity = old_quantity + quantity

        else:
            item = OrderItem(ingridient)
            item.quantity = quantity

            self.__order_items.append(item)
    
    def get_price(self):
        price = 0
        for item in self.__order_items:
            price = price + item.get_price()
        
        return price

    def get_info(self):
        order = "\nYour order:\n"
        for item in self.__order_items:
            order = order + item.get_info()
    
        return order
    
    def print_order(self):
        order_description = self.get_info()
        order_description = order_description + "Price: " + str(self.get_price()) + "\n"
        print(order_description)