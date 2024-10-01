# Class practice - OOP
# elevator class

class Elevator:
    def __init__(self):
        self.floor = 1
        self.num_pass = 0
        self.doors_open = False
    def get_floor(self):
        return self.floor
    def get_num_pass(self):
        return self.num_pass
    def call_to_floor(self, newfloor):
        self.floor = newfloor
        self.doors_open = False
        pass
    def enter_pass(self, num):
        if self.doors_open == False:
            print("Doors are closed!")
        elif self.doors_open == True:
            self.num_pass += num
        return self.num_pass
    def exit_pass(self, num):
        if self.doors_open == False:
            print("Doors are closed!")
        elif self.doors_open == True:
            self.num_pass -= num 
        return self.num_pass
    def open_doors(self):
        self.doors_open = True
        pass

e = Elevator()

e.call_to_floor(4)
print(e.get_floor())

e.open_doors()
e.enter_pass(2)
print(e.num_pass)
e.call_to_floor(5)
e.exit_pass(1)
e.open_doors()
e.exit_pass(1)
print(e.num_pass)
print(e.get_floor())

