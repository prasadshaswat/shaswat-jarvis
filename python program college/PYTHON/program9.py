#a program that  generted multiplication table of a number
def table(n):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
n=int(input("Enter the number:"))
table(n)
if __name__ == "__main__":
    pass
#out