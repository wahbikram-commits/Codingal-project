A=int(input("enter a value"))
B=int(input("enter a value"))
C=int(input("enter a value"))

avg=(A+B+C)/3

if avg>A and avg>B and avg>C:
    print(f"{avg} is greater than {A}, {B} and {C}")
elif avg>A and avg>B:
    print(f"{avg} is greater than {A}, {B}")
elif avg>A and avg>C:
    print(f"{avg} is greater than {A},{C}")
elif avg>B and avg>C:
    print(f"{avg} is greater than {B},{C}")
elif avg>A:
    print(f"{avg} is greater than {A}")
elif avg>B:
    print(f"{avg} is greater than {B}")
elif avg>C:
    print(f"{avg} is greater than {C}")