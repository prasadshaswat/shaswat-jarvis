# a program that conversts a given number form one bas to another decimal binary octal an hexadecimal vice versa
def decimal_to_binary(n):
    return bin(n).replace("0b","")
def decimal_to_octal(n):
    return oct(n).replace("0o","")
def decimal_to_hexadecimal(n):
    return hex(n).replace("0x","")
def binary_to_decimal(n):
    return int(n,2)
def octal_to_decimal(n):
    return int(n,8)
def binary_to_octal(n):
    return oct(int(n,2)).replace("0o","")
def binary_to_hexadecimal(n):
    return hex(int(n,2)).replace("0x","")
def octal_to_binary(n):
    return bin(int(n,8)).replace("0b","")
def octal_to_hexadecimal(n):
    return hex(int(n,8)).replace("0x","")
def hexadecimal_to_binary(n):
    return bin(int(n,16)).replace("0b","")
def hexadecimal_to_octal(n):
    return oct(int(n,16)).replace("0o","")
def hexadecimal_to_decimal(n):
    return int(n,16)
def main():
    while True:
        print("1.Decimal to Binary")
        print("2.Decimal to Octal")
        print("3.Decimal to Hexadecimal")
        print("4.Binary to Decimal")
        print("5.Octal to Decimal")
        print("6.Binary to Octal")
        print("7.Binary to Hexadecimal")
        print("8.Octal to Binary")
        print("9.Octal to Hexadecimal")
        print("10.Hexadecimal to Binary")
        print("11.Hexadecimal to Octal")
        print("12.Hexadecimal to Decimal")
        print("13.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            n=int(input("Enter the number:"))
            print("Binary:",decimal_to_binary(n))
        elif choice==2:
            n=int(input("Enter the number:"))
            print("Octal:",decimal_to_octal(n))
        elif choice==3:
            n=int(input("Enter the number:"))
            print("Hexadecimal:",decimal_to_hexadecimal(n))
        elif choice==4:
            n=input("Enter the number:")
            print("Decimal:",binary_to_decimal(n))
        elif choice==5:
            n=input("Enter the number:")
            print("Decimal:",octal_to_decimal(n))
        elif choice==6:
            n=input("Enter the number:")
            print("Octal:",binary_to_octal(n))
        elif choice==7:
            n=input("Enter the number:")
            print("Hexadecimal:",binary_to_hexadecimal(n))
        elif choice==8:
            n=input("Enter the number:")
            print("Binary:",octal_to_binary(n))
        elif choice==9:
            n=input("Enter the number:")
            print("Hexadecimal:",octal_to_hexadecimal(n))
        elif choice==10:
            n=input("Enter the number:")
            print("Binary:",hexadecimal_to_binary(n))
        elif choice==11:
            n=input("Enter the number:")
            print("Octal:",hexadecimal_to_octal(n))
        elif choice==12:
            n=input("Enter the number:")
            print("Decimal:",hexadecimal_to_decimal(n))
        elif choice==13:
            break
        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    main()
