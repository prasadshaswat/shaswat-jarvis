#a program that calvculate the area and perimeter of rectangle
def area_of_rectangle(l,b):
    return l*b
def perimeter_of_rectangle(l,b):
    return 2*(l+b)
if __name__ == "__main__":
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    print("Area: ", area_of_rectangle(length, breadth))
    print("Perimeter: ", perimeter_of_rectangle(length, breadth))
    print("the area of the rectangle is ",area_of_rectangle(length,breadth),"and the perimeter of the rectangle is ",perimeter_of_rectangle(length,breadth))