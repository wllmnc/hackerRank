#include<stdlib.h>
#include<stdio.h>

int**  multMatrix(int *MatrizA,int nRowA,int nColA,int *MatrizB,int nRowB,int nColB);

void multMatrix2(int *MatrizA,int nRowA,int nColA,int *MatrizB,int nRowB,int nColB)
{
	int Result[nRowA][nColB];
	if(nColA==nRowB)
	{
		for(int i=0;i<nRowA;i++)
		{
			int iValue=0;
			for(int j=0;j<nColA;j++)
			{
				printf("%d ",(&MatrizA[i])[j]);
			}
			printf("\n");
			//Result[i][j]=iValue;
		}
	}
	
}
void main(int argc, char *argv[])
{
	
	int nRowA=4;
	int nColA=4;
	int nRowB=4;
	int nColB=4;
	int matrizA[4][4]={{1,2,3,4},{1,2,3,4},{1,2,3,4},{1,2,3,4}};
	int matrizB[4][4]={{1,2,3,4},{1,2,3,4},{1,2,3,4},{1,2,3,4}};
	int** matrizC=multMatrix(&matrizA,nRowA,nColA,&matrizA,nRowB,nColB);
	//multMatrix2(&matrizA,nRowA,nColA,&matrizB,nRowB,nColB);
	for(int i=0;i<nRowA;i++)
	{
		for(int j=0;j<nColB;j++)
		{
			//printf(matrizC[i][j]+"\t");
		}
		printf("\n");
	}
	//printf("Hello world\n");
}

int**  multMatrix(int *MatrizA,int nRowA,int nColA,int *MatrizB,int nRowB,int nColB)
{
	int Result[nRowA][nColB];
	if(nColA==nRowB)
	{
		for(int i=0;i<nRowA;i++)
		{
			
			for(int j=0;j<nColA;j++)
			{
				int iValue=0;
				for(int k=0;k<nRowB;k++)
				{
					//
					printf("%d,%d* %d,%d",i,k,i+k,j);//(&MatrizA[i])[k],(&MatrizB[j])[k]);
					printf(" (%d*%d)",(&MatrizA[i])[k],(&MatrizB[i+k])[j]);
					int valTem=(&MatrizA[i])[k]*(&MatrizB[i+k])[j];
					iValue+=valTem;
					printf(":%d + ",valTem);
				}
				Result[i][j]=iValue;
				printf("=%d\t",iValue);
			//
			}
			printf("\n");
		}
		return Result;
	}
	return NULL;
	
}