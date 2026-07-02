Maths=int(input("Enter a marks for maths"))
Geography=int(input("Enter a marks for Geography"))
History=int(input("Enter a marks for History"))
Physics=int(input("Enter a marks for Physics"))
English=int(input("Enter a marks for English"))
Tot=Maths+Geography+History+Physics+English
Avg=Tot//5

Validrange=range(0,101)
if Avg not in Validrange:
    print("Invalid Average")
elif Avg in range(76,101):
    print("Excellent")
elif Avg in range(50,76):
    print("Good")
elif Avg in range(0,50):
    print("POOR")
