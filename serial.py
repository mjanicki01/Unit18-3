"""Python serial number generator."""

class SerialGenerator:
    """
    A class used to create unique incrementing serial numbers
    
    Attributes
    ----------------------------
    a: int
        The starting interger of the state of serial number
    """

    def __init__(self, a):
        self.a = a
        self.b = a

    def generate(self):
        """Method used to print current state of the start number, increasing it by 1 after each print"""
        print(self.a)
        self.a = self.a + 1

    def reset(self):
       """Resets instantiated object to the original start number"""
       self.a = self.b


"""Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100

"""
