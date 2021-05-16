# +----------------------+
# | Open Close Principle |
# +----------------------+

# The open close principle should be open for extension, but closed for modification
# If the program or a code is modified, it would exponentially bring requirements for further modifications
# To all other areas where the code affects

# Here are a couple of guidelines to help you recognize when open/closed may be applicable.
# When you have algorithms that perform a calculation (cost, tax, game score, etc.): the algorithm will likely change over time.
# When you have data coming or going from the system: the endpoint (file, database, another system)
# is likely to change. So is the actual format of the data.


# Though the code is explained in the video, I found a better version in the internet which literally saves a lot of time.

# So the goal with open close principle is that you isolate instantiable logics into a common class.
# This isolation will leverage Polymorphism and Inheritence which would make the code extensible.

# In the below area, I would show both the wrong implementation and the right implementation

#--------------------------#
# Incorrect IMPLEMENTATION |
#--------------------------#

class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass


animals = [Animal("lion"), Animal("Mouse")]


def animal_sounds(animals: list):
    for animal in animals:
        if animal == 'lion':
            print('roar')

        elif animal.name == 'Mouse':
            print('squeak')


animal_sounds(animals)

# Whats wrong with the above implementation?
# Now the first miss is the logic in animal sounds.
# With million animals around, you cant put an else if statement for all of them.
# The would clog the code at the same time, you will also identify that if any small minor modification is made,
# it has to be done to all the parts of the program.

# Second miss is animal list. So if we are having a 100 animals, this list would not help in any way.
# If the list is having 100 animals we would need to search for the middle of all these animals. animals

#--------------------------#
#  CORRECT IMPLEMENTATION  |
#--------------------------#

# This is the isolation of the common items taken


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def make_sound(self):
        pass

# With the virtual method made, we have made it possible to extend the
# Animal class to do multiple Methods. At times, you would need to do the same.


class Lion(Animal):
    def make_sound(self):
        return "Roar"


class Mouse(Animal):
    def make_sound(self):
        return "Squeak"


class Peacock(Animal):
    def make_sound(self):
        return "Squawks"


class BengalTiger(Animal):
    def make_sound(self):
        return "Heavy Roar"

#------------------#
#  Another Example |
#------------------#


class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2


class SuperVIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 4

# You could extend the discount class to add different logic compared to throwing them in a
# if else statement which would modify the program
