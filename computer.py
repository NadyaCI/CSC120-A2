class Computer:

    # All the attributes
    description: str = ""
    processor_type: str = ""
    hard_drive_capacity: int = 0
    memory: int = 0
    operating_system: str = ""
    year_made: int = 0 
    price: int = 0
    # The constructor
    def __init__(self, description: str, processor_type: str, 
                 hard_drive_capacity: int,  memory: int, 
                 operating_system: str, year_made: int, price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        
    # Updates the price according to input
    def update_price(self, new_price: int):
        self.price=new_price
    
    # Updates the OS according to input
    def update_os(self, new_os: str):
        self.operating_system=new_os
