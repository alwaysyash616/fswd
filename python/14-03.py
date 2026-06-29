"""
Assignment: 14
Problem: 03
Topic: Match
Description: Write a python script to make a menu driven program in which user has to choose one of the option from four given options - 1)Odd-Even, 2)Positive - Non Positive, 3)Simple Interest and 4) find roots of quadratic equation. Match and execute appropriate code on user selection.
Date: 26-06-2026
"""

ch=int(input("Enter your choice\n1) Odd-Even\n2) Positive - Non Positive\n3) Simple Interest\n4) find roots of quadratic equation\nYour choice: "))
match ch:
    case 1:
        num=int(input("Enter a number: "))
        print("Odd") if num%2 else print("Even")
    case 2:
        num=int(input("Enter a number: "))
        print("Positive") if num>0 else print("Non Positive")
    case 3:
        p=int(input("Enter principal amount: "))
        r=float(input("Enter rate of interest: "))
        t=int(input("Enter number of years: "))
        si=(p*r*t)/100
        print("Simple Interest:",si)
    case 4:
        print("Enter values of a,b,c")
        a,b,c=int(input()),int(input()),int(input())
        sqrt_d=(b**2-4*a*c)**0.5
        x1,x2=(-b+sqrt_d)/(2*a),(-b-sqrt_d)/(2*a)
        print("Roots: x1 =",x1,"x2 =",x2)
    case _:
        print("Wrong choice")