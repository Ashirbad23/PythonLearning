print("Hi")
name = input("What is your name?\n")
print("Hi " + name + ", welcome to Ashu's coffee.\n\n")
menu = "01: Black Coffee\n02: Espresso\n03: Latte\n04: Cappucino\n05: Kadak Masala Chai/Tea\n06: Lemon Tea"
print("Hey " + name + ", what you might like to order from our menu given below!\n" + menu)
order = input("Enter the serial no. of the drink you want: ")
if order == "01":
    drinks = "Black Coffee"
elif order == "02":
    drinks = "Espresso"
elif order == "03":
    drinks = "Latte"
elif order == "04":
    drinks = "Cappucino"
elif order == "05":
    drinks = "Kadak Masala Chai/Tea"
elif order == "06":
    drinks = "Lemon Tea"
else:
    print("Sorry for the inconvnience😔, but we have only six items now and we are planning to add more")

print( "Sounds good "+ name + ", your " + drinks + " is ready for you in a moment!😀")