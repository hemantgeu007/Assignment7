"""Q1"""
def calarea():
    r = float(input ("Input the radius of the circle : "))
    print ("The area of the circle with radius " + str(r) + " is: " + str(3.14 * r**2))

calarea()

"""Q2"""
def perfect(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    if sum == n:
        print(n)

for i in range(1,1001):
    perfect(i)

"""Q3"""
def mult_tab(n=12 , t = 1):
    if t == 11:
        return
    print(str(n) + " x " + str(t) + " = " + str(n*t))
    mult_tab(n, t+1)

mult_tab()

"""Q4"""
def power(a , b):
    if(b == 1):
        return(a)
    if(b != 1):
        return(a * power(a , b-1))

base = int(input("Enter base: "))
exp = int(input("Enter exponential value: "))

print("Result:",power(base,exp))

"""Q5"""
def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))

fact_dict = {}
n = int(input("Enter number:"))
fact_dict[n] = factorial(n)
print(fact_dict)