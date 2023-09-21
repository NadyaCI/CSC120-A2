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

    # The methods
    def buy(self, computer: Computer):
        global itemID
        self.itemID += 1
        itemID=self.itemID
        self.inventory[itemID] = computer
        print("Item", itemID, "purchased!\n")

    def sell(self, item: int):
        if item in self.inventory:
            del self.inventory[item]
            print("Item", item, "sold!\n")
        else:
            print("Item", item, "not found. Please select another item to sell.\n")

    def list_inventory(self):
        if self.inventory:
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

    print("Buying", new_computer.description)
    shop.buy(new_computer)

    print("Buying", another_computer.description)
    shop.buy(another_computer)

    print("Checking inventory...")
    shop.list_inventory()

    new_OS: str = "macOS Ventura"
    print("Refurbishing item ID 1, updating OS to", new_OS)
    shop.refurbish(1, new_OS)

    print("Checking inventory...")
    shop.list_inventory()

    print("Selling Item ID #")
    shop.sell(3)

    print("Selling Item ID 1")
    shop.sell(1)

    print("Checking inventory...")
    shop.list_inventory()

main()