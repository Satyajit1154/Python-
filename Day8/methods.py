'''Methods
    1.Instance Methods-
    This method accepts 1 st parameter self(instance)Parameter
     
    2.Class Methods-
    This Method accepts cls as 1st Parameter  and is called by cls keyword

    3.Static Methods-
    This are not class methods nor instance methods and strictly has no instance(self) and class(cls) Parameters in it.
'''

class Laptop:
    storage_type="ssd"

    #Constructor-
    def __init__(self,RAM,storage):
        self.RAM=RAM
        self.storage=storage

    #1. Instance Method
    def get_info(self):
        print(f"Laptop has {self.RAM} RAM and {self.storage}, {self.storage_type}")


    # 2. Class method
    @classmethod  #This is the decorater, decorater is special function used at top of the method to make it class method
    def get_storage_type(cls):
        print(f"Storage type={cls.storage_type}")


    @staticmethod
    def calc_discount(price,discount):
        final_price=price-(discount*price/100)
        print(f"Discounted price={final_price}")

        

l1=Laptop("16gb","512gb")
l2=Laptop("8gb","256gb")

l1.get_info() #instance variable called by object 

Laptop.get_storage_type() #Class method called by Class name
l1.calc_discount(40_000,10)