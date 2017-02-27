#!/bin/python
#https://www.hackerrank.com/contests/w29/challenges/a-circle-and-a-square
import math
import sys

class circle:
    _x,_y,_r=0,0,0
    
    def __init__(self, x, y, r):
        self._x, self._y, self._r= x, y, r
      
    def inCicle(self,x,y):
        return math.sqrt(math.pow((self._x-x),2)+math.pow((self._y-y),2))<=self._r
           
    
class square:
    _x1,_y1,_x3,_y3,_d=0,0,0,0,0
    _x2,_y2,_x4,_y4   =0,0,0,0
    _xc,_yc=0,0
    def __init__(self, x1, y1, x3, y3):
        self._x1, self._y1 = (x3, y3) if x1>x3 else (x1, y1)
        self._x3, self._y3 = (x1, y1) if x1>x3 else (x3, y3)
        
        mm= math.fabs(self._x1-self._x3) if math.fabs(self._x1-self._x3) < math.fabs(self._y1-self._y3) else (math.fabs(self._y1-self._y3) if  math.fabs(self._y1-self._y3) != math.fabs(self._x1-self._x3) else 0 )
        self._d =int( math.sqrt(math.pow((self._x1-self._x3),2)+math.pow((self._y1-self._y3),2)))
        yd= mm if self._y1!=self._y3  and self._x1!=self._x3 else (  (math.fabs(self._x1-self._x3))/2 if self._x1!=self._x3 else  math.fabs(self._y1-self._y3)/2)
        
        xl=self._x1
        xr=self._x3
        yt=self._y1 if self._y1<self._y3 else self._y3
        yb=self._y3 if self._y1<self._y3 else self._y1

        if self._y1>self._y3:
            self._x2,self._y2=xl,yt
            self._x4,self._y4=xr,yb
        else:
            self._x2,self._y2=xr,yt
            self._x4,self._y4=xl,yb
        
        if self._y1>self._y3:
            self._x2 = self._x2 + (  yd if math.fabs(self._x1-self._x3)> self._d/2 else -yd)
            self._x4 = self._x4 + ( -yd if math.fabs(self._x1-self._x3)> self._d/2 else yd)
            self._y2 = self._y2 + (  yd if math.fabs(self._y1-self._y3)> self._d/2 else -yd)
            self._y4 = self._y4 + (  -yd if math.fabs(self._y1-self._y3)> self._d/2 else yd)
        else:
            self._x2 = self._x2 + (  -yd if math.fabs(self._x1-self._x3)> self._d/2 else  yd)
            self._x4 = self._x4 + (   yd if math.fabs(self._x1-self._x3)> self._d/2 else -yd)
            self._y2 = self._y2 + (   yd if math.fabs(self._y1-self._y3)> self._d/2 else -yd)
            self._y4 = self._y4 + (  -yd if math.fabs(self._y1-self._y3)> self._d/2 else   yd)
        self._xc, self._yc = self._x1 + self._d/2, (self._y1 if self._y1>self._y3 else self._y3) - math.fabs(self._y1-self._y3) /2
        #print self._d , yd, mm
        #print self._x1, self._y1
        #print self._x2, self._y2
        #print self._x3, self._y3
        #print self._x4, self._y4
        #print self._xc, self._yc
        
    def triangleArea(self,A,B,C):
        Ax,Ay=A
        Bx,By=B
        Cx,Cy=C
        return (Cx*By-Bx*Cy)-(Cx*Ay-Ax*Cy)+(Bx*Ay-Ax*By)
    
    def inSquare(self, x, y):
        A=self._x1, self._y1
        C=self._x3, self._y3
        B=(self._x2, self._y2) #if self._y3>self._y1 else (self._x4, self._y4)
        D=(self._x4, self._y4) #if self._y3>self._y1 else (self._x2, self._y2) 
        P=x,y
        return False if self.triangleArea(A,B,P)>0 or self.triangleArea(B,C,P)>0 or self.triangleArea(C,D,P)>0 or self.triangleArea(D,A,P)>0 else True

w,h = map(int,raw_input().strip().split(' '))
circleX,circleY,r = map(int,raw_input().strip().split(' '))
x1,y1,x3,y3 = map(int,raw_input().strip().split(' '))
_circle=circle(circleX,circleY,r)
_square=square(x1,y1,x3,y3)
for y in xrange(h):
    raw=""
    for x in range(w):
        raw+=("#" if (_square._xc<=w and _square._yc<=h and _square.inSquare(x,y)) else ".")
    print raw
# _square._xc<=w and _square._yc<=h and
