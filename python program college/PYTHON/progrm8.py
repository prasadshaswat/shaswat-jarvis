#list item  ascending order $ descending order
def list_item():
    number = int(input("Enter the number of elements to be inserted: "))
    arr = list(map(int, input("Enter the elements: ").strip().split()))[:number]
    print("The list in ascending order is ",sorted(arr))
    print("The list in descending order is ",sorted(arr,reverse=True))
if __name__ == "__main__":
    list_item()