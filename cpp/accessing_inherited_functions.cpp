//https://www.hackerrank.com/challenges/accessing-inherited-functions?h_r=next-challenge&h_v=zen
#include<iostream>

using namespace std;

int callA=0;
int callB=0;
int callC=0;
class A
{
protected:
   
   void func(int  & a)
   {
      a=a*2;
      callA++;
   }
};

class B
{
protected:
   void func(int & a)
   {
      a=a*3;
      callB++;
   }
};

class C
{
protected:
   void func(int & a)
   {
      a=a*5;
      callC++;
   }
};

class D: public A, public B, public C
{
	int val;
	public:
		//Initially val is 1
		 D()
		 {
		 	val=1;
		 }


		 //Implement this function
		 void update_val(int new_val)
		 {
             while(new_val>1){
                 
                if (new_val%2==0){
                    this->A::func(val);
                    new_val=new_val/2;
                }else{
                    if (new_val%3==0){
                        this->B::func(val);
                        new_val=new_val/3;
                        }else{
                            if (new_val%5==0){
                                this->C::func(val);
                                new_val=new_val/5;
                            }
                         }
                    }
             };
		 }
		 //For Checking Purpose
		 void check(int); //Do not delete this line.
};
