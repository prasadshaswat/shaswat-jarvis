#a program check if a number is prime or not and leap year
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
if __name__ == "__main__":
    while True:
        print("Options:")
        print("Enter '1' to check if a number is prime")
        print("Enter '2' to check if a year is a leap year")
        print("Enter '3' to quit")
        user_input = input(": ")
        if user_input == "1":
            num = int(input("Enter number: "))
            print("Prime: ", is_prime(num))
        elif user_input == "2":
            year = int(input("Enter year: "))
            print("Leap year: ", leap_year(year))
        elif user_input == "3":
            break
        else:
            print("Invalid input")
            