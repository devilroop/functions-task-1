# check palidromine or not
def example1(a):
    if a==a[::-1]:
        print(a,"is palindrome ")
    else:
        print(a," is not polindrome")
    return a

example1("malayalam")
#when number is even or odd
def function(num):
    if num%2==0:
        print(num,"is even number")
    else:
        print(num,"is odd number")
    return num
function(6)
# check a number is negitive or positive 
def function (num):
    if num>0:
        print(num,"is positive")
    else:
        print(num,"is negitive")
    return num
function(-9)
# program (a+b)(a-b)
def function (a,b):
    x=a+b
    y=a-b
    z=x*y
    return z
a=int(input("first number="))
b=int(input("second number="))
result=function(a,b)
print(result)

# program (a+b)(a-b)(a-c)
def function (a,b,c):
    x=a+b
    y=a-b
    v=a-c
    z=x*y*v
    return z
a=int(input("first number="))
b=int(input("second number="))
c=int(input("third number="))
result=function(a,b,c)
print(result)
