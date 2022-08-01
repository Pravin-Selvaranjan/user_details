print("Hello and welcome to the user detail game")
print("Please enter your details below")
print("What is your first name?")
first_name = input()
age = 29
print("What is your last name?")
last_name = input()
print("Hello" + " " + (first_name.capitalize()) + " " + (last_name.capitalize()))
print("Now" + " " + (first_name.capitalize()) + "," + " " + "I hear you are" +" " + (str(age)) + " " + "years of age, is that correct?")
answer = input("enter yes or no: ")
if answer == "yes":
    print("That's brilliant" + "," + "your name is" + " " + (first_name.capitalize()) + " " + "and you are" + " " + (
        str(age)) + " " + "years young!")

else:
    print("Oh dear!, my sincerest apologies. Let's get you back on track" + " " + (
        first_name).capitalize() + "." + " " + "How old are you?")
    age = int(input())

print("Using digits, type your house number")
house_number = int(input())
print("What is the name of your road?")
road_name = input()
print("What Town do you live in?")
town_name = input()
print("and finally, your postcode please")
post_code = input()

if age > 18:
    print("Thank you for all of that information" + " " + (first_name.capitalize()) + " " + (last_name[0].capitalize()) + "," + " " + "your age is " + str(age) + " and your address is" + " " + (house_number) + " " + (road_name.title()) + "," + " " + (town_name.title()) + "," + " " + (post_code.upper()) + ".")
else:
    print("Unfortunately you are underage, please come back in " + str(18-age) + " years.")















