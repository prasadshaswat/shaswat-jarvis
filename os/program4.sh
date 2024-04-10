dd=0
mm=0
yyyy=0
days=0
echo -n "Enter the date in the format of dd "
read dd
echo -n "Enter the month in the format of mm "
read mm
echo -n "Enter the year in the format of yyyy "
read yyyy
if [ $mm -eq 1 -o $mm -eq 3 -o $mm -eq 5 -o $mm -eq 7 -o $mm -eq 8 -o $mm -eq 10 -o $mm -eq 12 ]
then
    days=31
elif [ $mm -eq 4 -o $mm -eq 6 -o $mm -eq 9 -o $mm -eq 11 ]
then
    days=30
elif [ $mm -eq 2 ]
then
    if [ `expr $yyyy % 4` -eq 0 -a `expr $yyyy % 100` -ne 0 -o `expr $yyyy % 400` -eq 0 ]
    then
        days=29
    else
        days=28
    fi
else
    echo "Invalid month"
fi
if [ $dd -le $days ]
then
    echo "Date is $dd/$mm/$yyyy"
else
    echo "Invalid date"
fi