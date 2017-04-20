#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <ctype.h>

int main()
{
   FILE *fptr;
   char input[255];
   char *status1;

   fptr = fopen("test.txt", "r");
   int line=1;
   if(fptr == NULL)
   {
      printf("Can not open file 1!\n");
   }
   else
   {
    char c ;
    printf("line %i",line++);

    do{
        c = fgetc(fptr);
        if(c=='\n')
        printf("\nline %i",line++);
        else
        printf ("%c", c);

    }while (c != EOF);

   }
   fclose(fptr);
   return 0;
}
