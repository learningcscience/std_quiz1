#function to find if a given number is prime or not
#assigned: mohan
def is_prime(n):
    pass


#function to rotate a given string n times
#assigned: mahendra
def rotate_string(s, n):
 
    s = list(s)  
    t= ""
    r = ""  
    c=""

    for i in range(n):
        if len(s) > 0:
            t = s.pop()  
            s.insert(0,t)
            
            c= "".join(s)

         
    return c



#function to find the factorial of a given number
#assigned: bastola
def factorial(n):
    pass


#function to find the nth Fibonacci number
#assigned: mohan
def fibonacci(n):
    pass


#function to find the GCD of two numbers
#assigned: mahendra
def gcd(a, b):
    if a<b:
       i=a
    else:
        i=b
    for i in range(i,0,-1):
        if a%i==0 and b%i==0:
            return i
        


#function to find the LCM of two numbers
#assigned: bastola
def lcm(a, b):
    pass


#function to find the square root of a given number
#assigned: mohan
def square_root(n):
    pass


#function to find the sum of digits of a given number
#assigned: mahendra
def sum_of_digits(n):
    convertstr = str(n)  
    sum = 0
    for i in convertstr:
        c = int(i)        
        sum += c         
    return sum





#function to find the reverse of a given string
#assigned: bastola
def reverse_string(s):
    pass







