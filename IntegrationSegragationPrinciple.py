from abc import abstractmethod
# +---------------------------------+
# | Interface Segregation Principle |
# +---------------------------------+

# Actually, This principle suggests that “A client should not be forced to implement an interface that it does not use”


# No client should be foreced to depend on methods it doesnt use
# An interface should describe one set of behaviours


# INCORRECT VERSION

# If you check out the coffee machine, you could see that it makes 3 types of coffee.
# But if you implement a dedicated espresso machine, then it also inherits the latte and capuccino
# Ofcourse we would love a machine that makes all kinds of coffee but here the deal is that the espresso machine should make only espresso
# If I need all the types of coffee, I would go for a coffee machine not an espresso machine
# So the idea is if espresso machine is inheriting qualities from coffee machine, it shouldnt unncessarily inherit qualities to make latte or capuccino

# class coffeeMachine:

#     def make_latte(self):
#         raise NotImplemented

#     def make_espresso(self):
#         raise NotImplemented

#     def make_capuccino(self):
#         raise NotImplemented


# class CoolCoffeeMachine(coffeeMachine):
#     def make_latte(self):
#         print("Latte Is done!")

#     def make_espresso(self):
#         print("Espresso is made")

#     def make_capuccino(self):
#         print("Capuccino is made")


# class EspressoMachine(coffeeMachine):
#     def make_espresso(self):
#         print("Making esspresso")


# if __name__ == "__main__":
#     CoolCoffeeMachine.make_latte()


# +------------------------------+
# CORRECT VERSION
# +------------------------------+

# when you encounter problems like this the best solution is to assign individual class to the coffees

class LatteMaker:
    @abstractmethod
    def make_latte(self):
        raise NotImplementedError


class EspressoMaker:
    @abstractmethod
    def make_espresso(self):
        raise NotImplementedError


class CapuccinoMaker:
    @abstractmethod
    def make_capuccino(self):
        raise NotImplementedError


class CoolCoffeeMachine(LatteMaker, EspressoMaker, CapuccinoMaker):

    def make_latte(self):
        print("Latte Is done!")

    def make_espresso(self):
        print("Espresso is made")

    def make_capuccino(self):
        print("Capuccino is made")


class EspressoMachine(EspressoMaker):

    def make_espresso(self):
        print("Making esspresso")


if __name__ == "__main__":
    CoolCoffeeMachine.make_latte("coffee")
    EspressoMachine.make_espresso("coffee")
