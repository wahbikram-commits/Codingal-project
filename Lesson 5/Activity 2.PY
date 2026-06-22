cp=int(input("Enter the cost price"))
sp=int(input("Enter the selling price"))

if sp>cp:
    print("You made profit")
    print("profit=", sp-cp)
else:
    print("No profit")