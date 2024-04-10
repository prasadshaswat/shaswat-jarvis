#a program that calculate the avg list of numbers
number = int(input("Enter the number of elements to be inserted: "))
arr = list(map(int, input("Enter the elements: ").strip().split()))[:number]
sum=0
for i in arr:
    sum+=i
avg=sum/number
print("The average of the elements in the list is ",avg)

#or alternatively
number1 = int(input("Enter the number of elements to be inserted: "))
arr=[]
for i in range(number1):
    arr.append(int(input("Enter the elements: ")))
sum1=0
for i in arr:
    sum1+=i
avg1=sum1/number1
print("The average of the elements in the list is ",avg1)
