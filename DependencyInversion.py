#================================#
# Dependency Inversion Priciple  |
#================================#

# Goal

# High-level modules should not depend on low-level modules. Both should depend on abstractions (e.g. interfaces).
# Abstractions should not depend on details. Details (concrete implementations) should depend on abstractions

# EXAMPLE PROGREAM


from abc import ABC, abstractmethod


class Switchable(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print("Light Bulb Turned On....")

    def turn_off(self):
        print("Light Bulb Turned Off...")


class Fan(Switchable):
    def turn_on(self):
        print("Fan Turned On....")

    def turn_off(self):
        print("Fan Turned Off...")


class ElectricPowerSwitch:

    def __init__(self, c: Switchable):
        self.Switchable = c
        self.on = False

    def press(self):
        if self.on:
            self.Switchable.turn_off()
            self.on = False
        else:
            self.Switchable.turn_on()
            self.on = True


l = LightBulb()
light_switch = ElectricPowerSwitch(l)
light_switch.press()
light_switch.press()
f = Fan()
fan_switch = ElectricPowerSwitch(f)
fan_switch.press()
fan_switch.press()
