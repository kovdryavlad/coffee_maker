from classes import *

class CoffeService:
    def __init__(self):
        self.__ingridients = []

    def init(self):
        ing1 = Ingridient("milk")
        ing1.price = 5

        ing2 = Ingridient("sugar")
        ing2.price = 2

        self.__ingridients = [ing1, ing2]

    def print_menu(self):
        print ("Menu:")
        for idx, ing in enumerate(self.__ingridients):
            print(idx, "-->", ing.get_info())

    def start_service_loop(self):
        order = Order()
        while(True):
            inp = input("Please type id of ingridient: ")
            if inp == "exit":
                break
            if inp == "new":
                order = Order()
            else:
                try:
                    order.add_ingridient(self.__ingridients[int(inp)], 1)
                except:
                    print("Invalid input. Please, try again")
            order.print_order()

if __name__ == "__main__":
    coffee_service = CoffeService()
    coffee_service.init()
    coffee_service.print_menu()
    coffee_service.start_service_loop()