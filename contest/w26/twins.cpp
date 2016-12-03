//https://www.hackerrank.com/contests/w26/challenges/twins
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

struct Node
  {
     int data;
     struct Node *next;
  };
Node* Insert(Node *head,int data)
{
   // Complete this method
    Node *headbk=head;
    Node *current=head;
    while(current!=NULL && current->next!=NULL)
    {
        current=current->next;
    }
    Node *newNode=(Node*)malloc(sizeof(Node));
    newNode->data=data;
    newNode->next=NULL;
    if(headbk!=NULL)
        current->next=newNode;
    else
        headbk=newNode;
    return headbk;
}
void Print(Node *head)
{  
  Node *current=head;
  while(current!=NULL)
  {
      printf("%d\n",current->data);
      current=current->next;
  }
}
int getModuleCount(Node *head,int data,int module)
{  
  Node *current=head;
  int count=0;
  while(current!=NULL)
  {
      if(current->data!=data && abs(current->data-data)==module)count++;
      current=current->next;
  }
  return count;
}


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n,m,i;
    scanf("%d",&n);    
    scanf("%d",&m);
    int flag=0,count=0;  
    
    Node *LLPrimes=NULL;
    
    while (n <= m)
    {
        while(n<=1)n++;
        flag = 0;
        for(i = 2; i <= n/2; ++i)
        {
            if(n % i == 0)
            {
                flag = 1;
                break;
            }
        }
        if (flag == 0)
            LLPrimes=Insert(LLPrimes,n);
        ++n;
    }
    //Print(LLPrimes);
    
    Node *iterator=LLPrimes;
    while(iterator!=NULL)
    {
        count+=getModuleCount(iterator,iterator->data,2);
        iterator=iterator->next;
    }
    printf("%d",count);
    
    return 0;
}
