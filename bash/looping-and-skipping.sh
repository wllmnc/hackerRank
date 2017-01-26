#https://www.hackerrank.com/challenges/bash-tutorials---looping-and-skipping
X=1
while [ $X -le 99 ]
do
    if (( $X % 2 == 1 ))
    then
	   echo $X
    fi
	X=$((X+1))
done
