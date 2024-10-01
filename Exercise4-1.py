# Exercise 4-1: Nested Loops and Lists

x = [20, 32, 40]
y = [2, 5]

def compare(x: list[int], y: list[int]):
    flag: bool = False
    for n in x: 
        for i in y: 
            if n % i == 0: 
                flag = True
            else: 
                flag = False 
                print(f"X: {n}, Y: {i}")
                return flag
    return flag

print(compare(x, y))