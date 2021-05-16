# +---------------------------------+
# | Liskov's Substitution Principle |
# +---------------------------------+

# Lets see whats so crytptic about this one..

# If you have an interface that takes up a base class,
# you should be able to stick a derived class in which
# everthing should work

# Here is another explanation which is in allusion to this


# In the below program, We have defined a single class called vehicle.
# Now in this class, you could all the functionalities of the vehicle such as
# Engine, speed and other stuffs.
# Comming to this program, when we substitute the vehicle class to different other classes,
# We should not get any contradictory error results.

# +-------------------+
# | INCORRECT VERSION |
# +-------------------+


class Vehicle:
    """A demo Vehicle class"""

    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def get_name(self) -> str:
        """Get vehicle name"""
        return f"The vehicle name {self.name}"

    def get_speed(self) -> str:
        """Get vehicle speed"""
        return f"The vehicle speed {self.speed}"

    def engine(self):
        """A vehicle engine"""
        pass

    def start_engine(self):
        """A vehicle engine start"""
        self.engine()

# Now 2 different classes are created in which 1 is Car, which is again a vehicle and Bicycle, which
# Is another vehicle.


class Car(Vehicle):
    """A demo Car Vehicle class"""

    def start_engine(self):
        pass


# Now in the below code, we could substitute the same class, but in this case, we identify that the Bicycle
# Inherits unecessary engine class which is not related to its Nature.


class Bicycle(Vehicle):
    """A demo Bicycle Vehicle class"""

    def start_engine(self):
        pass


# +-----------------+
# | CORRECT VERSION |
# +-----------------+

class Vehicle:
    """A demo Vehicle class"""

    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def get_name(self) -> str:
        """Get vehicle name"""
        return f"The vehicle name {self.name}"

    def get_speed(self) -> str:
        """Get vehicle speed"""
        return f"The vehicle speed {self.speed}"

# Now we have 2 different category of the vehicle principle.
# 1 being with an engine and the other without engine with different method.
# On Isolation you understand that no matter how you substitute the vehicle function
# you would get the proper and logical result without any errors.


class VehicleWithoutEngine(Vehicle):
    """A demo Vehicle without engine class"""

    def start_moving(self):
        """Moving"""
        raise NotImplemented


class VehicleWithEngine(Vehicle):
    """A demo Vehicle engine class"""

    def engine(self):
        """A vehicle engine"""
        pass

    def start_engine(self):
        """A vehicle engine start"""
        self.engine()

# On Subtituting the appropriate class in the car and bicycle functions we
# Could identify difference as well bring out the correct implementation of the function.


class Car(VehicleWithEngine):
    """A demo Car Vehicle class"""

    def start_engine(self):
        pass


class Bicycle(VehicleWithoutEngine):
    """A demo Bicycle Vehicle class"""

    def start_moving(self):
        pass

# Actually, LSP is a concept that applies to all kinds of polymorphism.
# Only if you don’t use polymorphism of all you don’t need to care about the LSP.
