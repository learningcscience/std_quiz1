from util import *



def lcm(a, b):
    
    greater = max(a,b)
    
    while True:
        if greater % a == 0  and greater % b == 0:
            lcm = greater
            break
        greater += 1
    print(f"the LCM of {a} and {b} is {lcm}")
    
lcm(4,6)
