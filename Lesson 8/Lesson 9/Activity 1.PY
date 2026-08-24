print("Pick your vehicle")
print(" 1.car")
print("2.Bike")
choice=int(input("Enter 1 or 2 ")) 
if choice == 1:
    print("select your car type")
    print("option 1, suv")
    print("option 2, sedan")
    cartype=int(input("suv or sedan"))
    if cartype == 1:
     print("you picked suv")
    else:
       print("you picked sedan")

    print("You picked car")
    print("top speed is 670kmh/h")
    print("good for driving with family")

else:
    print("you picked Bike")
    print("select your biketype")
    print("option 1, Mountain bike")
    print("option 2,Road bike")
    biketype=int(input("Mountain bike or Road bike"))
    if biketype == 1:
     print("You selected Mountainbike")
    else:
       print("You picked Roadbike")
    print("top speed is 170km/h")
    print("good for casual riding for 1 person and for fun")
