import json
from classes import *

#constants for work with json
INGRIDIENTS_FILE_PATH = "ingridients.json"
INGRIDIENTS_ONJECT_NAME = "ingridients"
INGRIDINT_NAME_STR = "name"
PRICE_STR = "price"

#constants for service loop
NEW_ORDER_STR = "new"
EXIT_STR = "exit"

class CoffeService:
    def __init__(self):
        self.__ingridients = []

    def init(self):
        with open(INGRIDIENTS_FILE_PATH) as json_file:
            data = {}
            try:
                data = json.load(json_file)
            except:
                print("Error with reading config file\n")
                return False

            for element in data[INGRIDIENTS_ONJECT_NAME]:
                try:
                    self.__ingridients.append(Ingridient(element[INGRIDINT_NAME_STR], element[PRICE_STR]))
                except:
                    print("Error in with ingridient\n")
            return True

    def print_menu(self):
        print ("Menu:")
        for idx, ing in enumerate(self.__ingridients):
            print(idx, "-->", ing.get_info())

    def start_service_loop(self):
        order = Order()
        order.print_order()
        while(True):
            inp = input("Please type id of ingridient for adding or service command: ")
            if inp == EXIT_STR:
                break
            if inp == NEW_ORDER_STR:
                order = Order()
            else:
                try:
                    order.add_ingridient(self.__ingridients[int(inp)], 1)
                except:
                    print("Invalid input. Please, try again")
            order.print_order()

if __name__ == "__main__":
    coffee_service = CoffeService()
    init_status = coffee_service.init()
    if init_status is not False:
        coffee_service.print_menu()
        coffee_service.start_service_loop()