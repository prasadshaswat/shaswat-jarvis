#calcualtor
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y
def power(x, y):
    
    return x ** y       
def square(x):
    
    return x ** 2
def sqrt(x):
    
    return x ** 0.5
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
def sin(x):
    import math
    return math.sin(x)
def cos(x):
    import math
    return math.cos(x)
def tan(x):
    import math
    return math.tan(x)
def log(x):
    import math
    return math.log(x)
if __name__ == '__main__':
    #whileloop
    while True:
        print('Select operation:')
        print('1. Add')
        print('2. Subtract')
        print('3. Multiply')
        print('4. Divide')
        print('5. Power')
        print('6. Square')
        print('7. Square root')
        print('8. Factorial')
        print('9. Sin')
        print('10. Cos')
        print('11. Tan')
        print('12. Log')
        print('13. Exit')
        #input
        choice = input('Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13): ')
        if choice in ('1', '2', '3', '4', '5'):
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number: '))
            if choice == '1':
                print('Result:', add(num1, num2))
            elif choice == '2':
                print('Result:', subtract(num1, num2))
            elif choice == '3':
                print('Result:', multiply(num1, num2))
            elif choice == '4':
                print('Result:', divide(num1, num2))
            elif choice == '5':
                print('Result:', power(num1, num2))
        elif choice in ('6', '7', '8', '9', '10', '11', '12'):
            num1 = float(input('Enter number: '))
            if choice == '6':
                print('Result:', square(num1))
            elif choice == '7':
                print('Result:', sqrt(num1))
            elif choice == '8':
                print('Result:', factorial(num1))
            elif choice == '9':
                print('Result:', sin(num1))
            elif choice == '10':
                print('Result:', cos(num1))
            elif choice == '11':
                print('Result:', tan(num1))
            elif choice == '12':
                print('Result:', log(num1))
        elif choice == '13':
            break
        else:
            print('Invalid Input')
            