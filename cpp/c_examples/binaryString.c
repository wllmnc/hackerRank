#include <stdio.h>


int* getBinary(char *string)
{
	int *array;
	int *array2=array;
		while(*string){
		int bit_i;
		for (bit_i = 7; bit_i >= 0; --bit_i) {
    		int bit=*string>>bit_i &1;
    		//printf("%d", bit);
    		*array=bit;
    		printf("%d", *array);
		}
		printf(" ");
		++string;
		++array;
	}
	return array2;
}

int main(int argn, char **argv)
{
	int *ArrayInt=getBinary(argv[1]);
	printf("%d", *ArrayInt); 
	while(*ArrayInt){
	printf("%d ", *ArrayInt);
	++ArrayInt;
	}
//printf("hola %s\n",sStrTemp);


	printf("\n");
	return 0;
}