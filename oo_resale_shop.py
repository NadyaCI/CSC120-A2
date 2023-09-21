from computer import Computer
from typing import Dict, Union, Optional

class ResaleShop:
    # What attributes will it need?
    #inventory, itemID
    inventory: Dict[int, Computer] = {}
    itemID: str = 0
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)    
    def __init__(self, inventory: Dict, itemID: int):
        self.inventory = inventory
        self.itemID=itemID

    def buy(self, computer: Computer):
        global itemID
        self.itemID+=1
        itemID=self.itemID
        self.inventory[itemID]=computer
        print("Item", itemID, "purchased!")

    def sell(self, item: int):
        del self.inventory[item]
        print("Item", itemID, "sold!")

    def list_inventory(self):
        for item in self.inventory:
            computer: str = ""
            print(f'Item ID: {item} : {self.inventory[item]}')

    #Buy, sell, store

add: Computer = Computer("sh","th",1,4,"sh",2,3)
print(add.price, add.operating_system)
add.update_price(72)
add.update_os("heehee")
print(add.price, add.operating_system)

shop=ResaleShop({},0)
shop.buy(add)
shop.list_inventory()