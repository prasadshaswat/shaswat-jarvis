def factorial():
    print("Enter the number to find the factorial:")
    n = int(input())
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial of the number is:", fact)

def check_palindrome():
    print("Enter the number to check palindrome:")
    try:
        k = int(input())
        temp = k
        rev = 0
        while k > 0:
            dig = k % 10
            rev = rev * 10 + dig
            k = k // 10
        if temp == rev:
            print("The number is a palindrome!")
        else:
            print("Not a palindrome!")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")



if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("Enter '1' to find the factorial of a number")
        print("Enter '2' to check if a number is palindrome")
        print("Enter '3' to quit")
        user_input = input(": ")
        if user_input == "1":
            factorial()
        elif user_input == "2":
            check_palindrome()
        elif user_input == "3":
            break
        else:
            print("Invalid input")
