A=5
B=10
C=0

#Using and operators
if A and B and C:
    print("All are true")
else:
    print("Atleast one number has boolean value false")


B=-10
if A>0 or B>0:
    print("One of the number is greater than 0")
else:
    print("neither of the numbers are greater than 0")


if C>0 or B>0:
    print("One of the number is greater than 0")
else:
    print("Neither of the numbers are greater than 0")