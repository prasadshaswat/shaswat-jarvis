#write a program check palindrome string or not
#!/bin/bash

read -p "Enter a string: " str
len=$(echo ${#str})
len=$(expr $len - 1)
i=1
j=$len
revstr=""

while [ $i -le $len ]
do
    rev=$(echo $str | cut -c $j)
    revstr="$revstr$rev"
    i=$(expr $i + 1)
    j=$(expr $j - 1)
done

if [ "$str" = "$revstr" ]
then
    echo "String is palindrome"
else
    echo "String is not palindrome"
fi