
#https://www.hackerrank.com/challenges/bash-tutorials---a-personalized-echoread name
echo "Welcome $name"
#https://www.hackerrank.com/challenges/bash-tutorials---looping-with-numbers
X=1
while [ $X -le 50 ]
do    
	echo $X   
	X=$((X+1))
done
#https://www.hackerrank.com/challenges/bash-tutorials---the-world-of-numbers
read X
read Y
echo  $(($X+$Y))
echo  $(($X-$Y))
echo  $(($X*$Y))
echo  $(($X/$Y))
