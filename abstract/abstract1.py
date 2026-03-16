from abc import *
class Operation(ABC):

    @abstractmethod
    def calculate(self, a, b):
        pass
class Addition(Operation):
    def calculate(self, a, b):
        print("Sum =", a + b)
class Multiplication(Operation):
    def calculate(self, a, b):
        print("Product =", a * b)
a1 = Addition()
m1 = Multiplication()

a1.calculate(5, 3)
m1.calculate(5, 3)