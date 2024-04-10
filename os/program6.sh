#write a shell scripit say good morning/afternoon/evening/night according to the system time
hour=$(date +%H)
if [ $hour -ge 6 -a $hour -lt 12 ]
then
    echo "Good Morning"
elif [ $hour -ge 12 -a $hour -lt 16 ]
then
    echo "Good Afternoon"
elif [ $hour -ge 16 -a $hour -lt 20 ]
then
    echo "Good Evening"
else
    echo "Good Night"
fi
 