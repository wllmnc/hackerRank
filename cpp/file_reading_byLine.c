#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <ctype.h>

int main()
{
   FILE *infile;
   char input[255];
   char *status1;

   infile = fopen("test.txt", "r");
   if(infile == NULL)
   {
      printf("Can not open file 1!\n");
   }
   else
   {
      do
      {
        //status1 = fscanf(infile, "%s", &input);
         status1 = fgets(input, sizeof(input), infile);
        printf("File 1: %s\n ", input);
     }while(status1);
   }
   fclose(infile);
   return 0;
}
