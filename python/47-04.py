"""
Assignment: 47
Problem: 04
Topic: Polymorphism
Description: Define a class Matrix with member variables rows, columns and a list to hold matrix elements. Overload + operator to add two matrix objects.
Date: 30-07-2026
"""

class Matrix:
    def __init__(self,a,b,c,d,e,f,g,h,i):
        self.r1=[a,b,c]
        self.r2=[d,e,f]
        self.r3=[g,h,i]
    def __add__(self,other):
        m1=[self.r1,self.r2,self.r3]
        m2=[other.r1,other.r2,other.r3]
        temp=list()
        i,j=0,0
        while i<=2:
            j=0
            while j<=2:
                temp.append(m1[i][j]+m2[i][j])
                j+=1
            i+=1
        return Matrix(*temp)
    def printMatrix(self):
        i,j,temp=0,0,[self.r1,self.r2,self.r3]
        while i<=2:
            j=0
            while j<=2:
                print(temp[i][j],end=' ')
                j+=1
            print()
            i+=1
m1=Matrix(1,2,3,4,5,6,7,8,9)
m2=Matrix(11,12,13,14,15,16,17,18,19)
m3=m1+m2
m1.printMatrix()
m2.printMatrix()
m3.printMatrix()
