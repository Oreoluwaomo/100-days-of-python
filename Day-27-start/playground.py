# *args
def add(*args):
    print(sum(args))
    # indexing
    print(args[0])
add(3,5,6)

# **kwargs
def calculate (**kwargs):
    print(kwargs)
    print(kwargs["add"])
    # for keys,values in kwargs.items():
    #     print(keys)
    #     print(values)
calculate(add=4,multiply=8,divide=12)

# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)




