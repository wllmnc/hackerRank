#include<stdlib.h>
#include<stdio.h>

int mirror(int number);

void main(int argc, char *argv[])
{
	
	int number=16;
	printf("\nresult=%d",mirror(number));
}

int mirror(int number)
{
	int result=0;
	int aNumber[8]={0};
	int cont=7;
	while(number>1)
	{
		if(number%2==1)
		{
			aNumber[cont]=1;
		}
		number=number/2;
		cont--;
	}
	if(number==1)
	{
		aNumber[cont]=1;
	}
	int i;
	for(i=0;i<8;i++)
	{
		result+=aNumber[i]*pow(2,i);
	}
	return result;
}
