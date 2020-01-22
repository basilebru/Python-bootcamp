import time
import getpass
import functools
from random import randint
from time import perf_counter

f = open("machine.log", "w+")
username = getpass.getuser()

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        p1 = perf_counter()
        r = func(*args, **kwargs)
        p2 = perf_counter()
        p3 = str(p2 - p1)[:5]
        f.write("(" + username + ")" + "Running: " + func.__name__
        +"     [ exec-time = " + p3 + "ms ]\n")
        return(r)
    return(wrapper)

class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
     if self.water_level > 20:
         return True
     else:
         print("Please add water!")
         return False

    @log
    def boil_water(self):
        return "boiling..."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(2):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 1))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    
    machine = CoffeeMachine()
    for i in range(0, 5):
        #machine.wrapper(x)                
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)