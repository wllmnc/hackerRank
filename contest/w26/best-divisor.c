https://www.hackerrank.com/contests/w26/challenges/best-divisor
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int getsum(int val);
int main(){
    int n; 
    scanf("%d",&n);    
    int arr[n];
    int cont=0;
    for(int i=n;i>0;i--)
    {
        if(n%i==0)
        {
            arr[cont++]=i;
        }
    }
    int max=getsum(arr[0]);
    int res=arr[0];
    for(int i=1;i<cont;i++)
    {
        if(max<getsum(arr[i])){
            max=getsum(arr[i]);
            res=arr[i];
        }else{
            if(max==getsum(arr[i]))
                if(res>arr[i])res=arr[i];               
        }
    }
    printf("%d",res);
    return 0;
}
int getsum(int val)
{
    int res=val;
    int ans=0;
    int valtemp=0;
      while(res>0){
      valtemp=res%10;
      ans+=valtemp;
      res=(res-valtemp)/10;
    }
    return ans;
}
