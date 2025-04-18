#function to find if a given number is prime or not
#assigned: mohan
def is_prime(n):
    if n <= 1:
        return False
        

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        
        i += 1

    return True


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
     
    if n < 0:
        print("Factorial does not exist for negative numbers")
        
    elif n == 1 or n ==0:
         print(f"The factorial of {n} is 1 ")
    
    else :
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        print(f"The factorial of {n} is {fact}")

#function to find the nth Fibonacci number
#assigned: mohan
def fibonacci(n):
    if n <= 0:
        print("Incorrect input")
        
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    



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
    larger = max(a,b)
    
    while True:
        if larger % a == 0 and larger % b == 0:
            lcm = larger 
            break
        larger += 1
        
    print(f"The LCM of {a} and {b} is {lcm}")

#function to find the square root of a given number
#assigned: mohan
def square_root(n):
    
    i = 1

    while i * i <= n:
        if i * i == n:
          print("Square root of", n, "is", i)
        i += 1
    

square_root(64)
     


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
   
   str = ""
   
   for i in s:
       str = i + str
   print(f"The reverse of {s} is {str}")
    






