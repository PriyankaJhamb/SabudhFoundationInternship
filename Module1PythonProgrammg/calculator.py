def sumnum(n, m):
    return n+m
def multnum(n, m):
    return  n*m
def divnum(n, m):
    return n/m
def subnum(n, m):
    return n-m


num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
choose=input("Enter +, *, /, - ")
if choose=='+':
    print("Sum: ",sumnum(num1, num2))
elif choose=='/':
    print("Divide: ",divnum(num1, num2))
elif choose=='*':
    print("Multiply: ",multnum(num1, num2))
elif choose=='-':
    print("Subtract: ",subnum(num1, num2))
else:
    print("Kindly Enter correct choice.")

