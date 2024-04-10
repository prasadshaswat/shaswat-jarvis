#a program that converts  temp in fahrenheit to celsius and vice versa while loop
def fahrenheit_to_celsius(f):
    return (f - 32) * 5.0/9.0
def celsius_to_fahrenheit(c):
    return c * 9.0/5.0 + 32
if __name__ == "__main__":
    while True:
        print("Options:")
        print("Enter '1' to convert Fahrenheit to Celsius")
        print("Enter '2' to convert Celsius to Fahrenheit")
        print("Enter '3' to quit")
        user_input = input(": ")
        if user_input == "1":
            f = float(input("Enter Fahrenheit: "))
            print("Celsius: ", fahrenheit_to_celsius(f))
        elif user_input == "2":
            c = float(input("Enter Celsius: "))
            print("Fahrenheit: ", celsius_to_fahrenheit(c))
        elif user_input == "3":
            break
        else:
            print("Invalid input")       