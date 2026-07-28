"""
Assignment: 47
Problem: 02
Topic: Polymorphism
Description: Overload greater than (>) operator in Time class which has instance object variables hour, min, sec.
Date: 26-07-2026
"""

class Time:
    def __init__(self,hh,mm,ss):
        self.hh=hh
        self.mm=mm
        self.ss=ss
        self.normalise()
    def showTime(self):
        print(self.hh,self.mm,self.ss,sep=':')
    def normalise(self):
        if self.ss>=60:
            self.mm+=self.ss//60
            self.ss%=60
        if self.mm>=60:
            self.hh+=self.mm//60
            self.mm%=60
    def evaluate(self):
        return (self.hh*60+self.mm)*60+self.ss
    def __gt__(self,other):
        if self.evaluate()>other.evaluate():
            return True
        else:
            return False

t1=Time(3,140,200)
t2=Time(2,245,343)  
t1.showTime()
print(">")
t2.showTime()
print(t1>t2)