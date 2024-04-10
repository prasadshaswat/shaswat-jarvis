    # #!/bin/bash

# Pattern 1
echo "Pattern 1:"
for ((i=1; i<=5; i++))
do
  for ((j=1; j<=i; j++))
  do
    echo -n "* "
  done
  echo
done

# Pattern 2
echo "Pattern 2:"
for ((i=1; i<=5; i++))
do
  for ((j=1; j<=i; j++))
  do
    echo -n "$j "
  done
  echo
done

# Pattern 3
echo "Pattern 3:"
num=1
for ((i=1; i<=5; i++))
do
  for ((j=1; j<=i; j++))
  do
    echo -n "$num "
    num=$((num+1))
  done
  echo
done

# Pattern 4
echo "Pattern 4:"
for ((i=1; i<=5; i++))
do
  for ((j=i; j<5; j++))
  do
    echo -n "  "
  done
  for ((k=1; k<=i; k++))
  do
    echo -n "$k "
  done
  for ((l=i-1; l>=1; l--))
  do
    echo -n "$l "
  done
  echo
done

# Pattern 5
echo "Pattern 5:"
num=1
for ((i=1; i<=5; i++))
do
  for ((j=1; j<=i; j++))
  do
    echo -n "$num "
    num=$((num+1))
  done
  echo
done