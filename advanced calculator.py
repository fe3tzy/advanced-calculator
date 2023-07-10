import math
operations = ['add','subtract','divide','multiply','exit']
#define math
def add(x,y):
    x+y
    return x+y
def subtract(x,y):
    x-y
    return x-y
def divide(x,y):
    x / y
    return x/y
def multiply(x,y):
    x*y
    return x*y


while True:
    #inputs
    num1 = float(input('What is the first number: '))
    num2 = float(input('What is the second number: '))
    #print options
    print(operations)
    #select operation
    choice = input('Select an operation: ').lower()
    
    #if statements
    if choice == 'add':
        z  = add(num1,num2)
        print(f'Solution: {z:.2f}')
    elif choice == 'subtract':
        c = subtract(num1,num2)
        print(f'Solution: {c:.2f}')
    elif choice == 'divide':
        a = divide(num1,num2)
        print(f'Solution: {a:.2f}')
    elif choice == 'multiply':
        b = multiply(num1,num2)
        print(f'Solution: {b:.2f}')
    elif choice == operations[4]:
        break
    else:
        continue
    
