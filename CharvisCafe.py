print("Hi")
name = input("What is your name?\n")
print("\nHi " + name + ", welcome to Charvis cafe.\n")
menu = """01: Coffee - ₹69
02: Black Coffee - ₹49
03: Espresso - ₹99
04: Latte - ₹109
05: Cappucino - ₹109
06: Cold Coffee - ₹69
07: Masala Tea - ₹69
08: Red Tea - 49
09: Lemon Tea - ₹89"""

if name == "Wanda" or name == "Moon Knight" or name == "Loki" or name == "Ultron" or name == "Zola" or name == "Thanos":
    test = input("Do to want to end the humman life from the earth?\n")
    if test == "yes":
        print("\nGet out you evil " + name + "😡🤬\n")
        exit()
    elif test == "no" and name == "Wanda" or name == "Moon Knight" or name == "Loki":
        test_allowed = input("Have you killed anyone innocent today?\n")
        if test_allowed == "yes":
            print("\nGet out you evil " + name + "😡🤬\n")
            exit()
    else:
        print("\nOhh you are one of the good " + name + ". Come on in\n") 

print("Hey " + name + ", what you might like to order from our menu given below!\n" + menu)
order = int(input("\nEnter the serial no. of the drink you want: "))
operation = {
    1:"Coffee",
    2:"Black Coffee",
    3:"Espresso",
    4:"Latte",
    5:"Cappucino",
    6:"Cold Coffee",
    7:"Masala Tea",
    8:"Red Tea",
    9:"Lemon Tea",
}
output = operation.get(order)

cost = {
    1: 69,
    2: 49,
    3: 99,
    4: 109,
    5: 109,
    6: 69,
    7: 69,
    8: 49,
    9: 89,
}
price = cost.get(order)

if output:
    quantity = int(input("How many cups would you like?\n"))
    total = price * quantity

if output:
    print("\nSounds good "+ name + ", your " + str(quantity) + " " + output + " will be ready for you in a moment!😀")
    print("You have total ₹" + str(total) + "\n")
else:
    print("\nError: Invalid input🤔🤔🤔\n")
    


