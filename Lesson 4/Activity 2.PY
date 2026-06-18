#Taking user input for amount
amount = int(input("Enter amount"))

#260
#100 pound bill
hundred=amount//100
fifty=(amount % 100)//50
ten=(amount % 50)//10

print("There are ",hundred, "hundred pound bills")
print("There are ", fifty, "fifty pound bills")
print("There are ", ten, "ten pound bills")