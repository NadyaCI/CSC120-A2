from computer import Computer
from typing import Dict, Union, Optional

class ResaleShop:
    # The attributes
    inventory: Dict[int, Computer] = {}
    itemID: str = 0
    
    # The constructor    
    def __init__(self, inventory: Dict, itemID: int):
        self.inventory = inventory
        self.itemID = itemID

    # Buy method, allows computers to be added to the inventory
    def buy(self, computer: Computer):
        global itemID
        self.itemID += 1    # Incrementally increases item ID
        itemID=self.itemID
        self.inventory[itemID] = computer   # Assigns new item in dictionary
        print("Item", itemID, "purchased!\n")

    # Sell method, removes item from inventory
    # By index, returns error message if index not in inventory
    def sell(self, item: int):
        if item in self.inventory:
            del self.inventory[item]
            print("Item", item, "sold!\n")
        else:
            print("Item", item, "not found. Please select another item to sell.\n")

    # List method, gives a list of all items in inventory
    def list_inventory(self):
        if self.inventory:  #If inventory is not empty
            for item in self.inventory:
                computer=self.inventory[item]
                print("Item ID", item, ": ", computer.description, ",", 
                      computer.processor_type, "processor,", 
                      computer.hard_drive_capacity, "hard drive capacity,", 
                      computer.memory, "memory,",
                      computer.operating_system, "operating system, made in",
                      computer.year_made, ", price", computer.price)
            print("All items listed.\n")
        else:
            print("No inventory to display.\n")

    # Refurbish method, updates price according to age of machine and optional OS update
    # By index, returns error message if index not in inventory
    def refurbish(self, item: int, new_os :Optional[str] = None):
        if item in self.inventory:
            computer = self.inventory[item]
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff
            if new_os!= None:
                computer.update_os(new_os)
                self.inventory[item] = computer
            print("Item", item, "has been refurbished!\n")

        else:
            print("Item", item, "not found. Please select another item to refurbish.\n")
            
def main():
    # Sets up shop and new computers
    shop: ResaleShop = ResaleShop({}, 0)
    new_computer: Computer = Computer("Mac Pro (Late 2013)",
                                      "3.5 GHc 6-Core Intel Xeon E5", 1024, 
                                      64, "macOS Big Sur", 2013, 1500)
    another_computer: Computer = Computer("Mac Pro (2020)", 
                                          "2 GHz Quad-Core Intel Core i5",
                                          512, 16, "macOS Ventura", 2020, 400)
    print("-" * 23)
    print("~COMPUTER RESALE STORE~")
    print("-" * 23, "\n")

    # Buys a new computer
    print("Buying", new_computer.description)
    shop.buy(new_computer)

    # Buys another computer
    print("Buying", another_computer.description)
    shop.buy(another_computer)

    # Checks inventory to confirm purchase
    print("Checking inventory...")
    shop.list_inventory()

    # Refurbishes computer 1 to new OS
    new_OS: str = "macOS Ventura"
    print("Refurbishing item ID 1, updating OS to", new_OS)
    shop.refurbish(1, new_OS)

    # Checks inventory to confirm refurbishment
    print("Checking inventory...")
    shop.list_inventory()

    # Tries to sell item not in inventory, returns error message
    print("Selling Item ID #")
    shop.sell(3)

    # Sells item 1
    print("Selling Item ID 1")
    shop.sell(1)

    # Checks inventory to confirm sale
    print("Checking inventory...")
    shop.list_inventory()

main()