#print given numbers and sum of them
echo "Enter the numbers"
read a
sum=0
while [ $a -ne 0 ]
do
sum=`expr $sum + $a`
read a
done
echo "Sum of the numbers is $sum"
#Output:
#Enter the numbers
#1
#2
#3
#4
#5
#0
#Sum of the numbers is 15
