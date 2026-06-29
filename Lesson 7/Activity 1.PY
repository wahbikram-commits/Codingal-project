A=5
if type(A) is int:
    print("A is an integer")
else:
    print("A is not an integer")


B=10.5
if type(B) is float:
    print("B is float type")
else:
    print("B is not a float type")


A=5
B=5
if A is B:
    print("A has the same identity of B")
else:
    print("A does not have the same identity of B")

B=10
if A is not B:
    print("A is not B")
else:
    print("A is B")
    