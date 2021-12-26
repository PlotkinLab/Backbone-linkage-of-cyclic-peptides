#!/bin/bash

# syntax shift filename lower bound upper bound
s=$(echo "$2-1" | bc)
for (( i=$2; i <= $3; i++))
do
    sed "s/ $i / $(echo "$i-$s" | bc) /g" $1 > temp
    mv temp $1
done
