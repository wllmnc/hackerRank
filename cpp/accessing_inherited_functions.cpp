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

class D 
{
    friend class A;
    friend class B;
    friend class C;
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
             A a=new A;
             B b=new B;
             C c=new C;
             a::func(new_val);
             b::func(new_val);
             c::func(new_val);
			
		 }
		 //For Checking Purpose
		 void check(int); //Do not delete this line.
};
