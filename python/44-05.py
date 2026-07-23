"""
Assignment: 44
Problem: 05
Topic: Decorator
Description: Write a function to check if the given sides of a triangle can form a valid triangle or not. Define a decorator to print “Right Angled Triangle” if the triangle is right angled triangle.
Date: 22-07-2026
"""

def rightTraingleCheckerGenerator(isT):
    def isRightTraingle(a,b,c):
        r=isT(a,b,c)
        if r and (a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2):
            print("Right Angled Traingle")
        return r
    return isRightTraingle

@rightTraingleCheckerGenerator
def isTraingle(a,b,c):
    return a>0 and b>0 and c>0 and a+b>c and b+c>a and a+c>b

r=isTraingle(-1,4,0)
print(r)