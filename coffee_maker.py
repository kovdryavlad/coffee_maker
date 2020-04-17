from classes import *

ing1 = Ingridient("milk")
ing1.price = 5

ing2 = Ingridient("sugar")
ing2.price = 2

order = Order()
order.add_ingridient(ing1, 1)
order.add_ingridient(ing2, 2)
#order.print_order()


ingrifients = [ing1, ing2]

print ("Menu:")
for idx, ing in enumerate(ingrifients):
    print(idx, "-->", ing.get_info())

order = Order()
order.print_order()
while(True):
    inp = input("Please type id of ingridient: ")
    if inp == "exit":
        break
    if inp == "new":
        order = Order()
    else:
        try:
            order.add_ingridient(ingrifients[int(inp)], 1)
        except:
            print("Invalid input. Please, try again")
    order.print_order()