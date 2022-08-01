# **_Python user detail task_**

## We will be using what we have learnt in the last week in order to create a simple user information programme. This will combine the following elements: 

- Strings
- Variables
- Integers
- Concatenation
- Casting


## _**Strings**_

```
my_string = 'Hello World'
print(my_string)
```
Strings can be created by enclosing characters inside a single quote or double-quotes. Even triple quotes can be used in Python but generally used to represent multiline strings and docstrings.

## **_Variables_**
```
x = 10
y = "Pravin"
print(x)
print(y)
```

You the user, must assign a value to the variable. Python has no command for declaring a variable.


## **_Integers_**
```
x = 1
y = 420
z = -6

print(type(x))
print(type(y))
print(type(z))
```
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.


## **_Concatenation_**
```
print("Hello" + " " + (first_name.capitalize()) + " " + (last_name.capitalize()))
```
Concatenation means joining strings together end-to-end to create a new string. To concatenate strings, we use the + operator. 

## **_Casting_**





In Python, Casting is a process in which we convert a literal of one type to another.
- int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
- float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
- str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals


### Combining all of the above I have put together a simple programme to showcase the functions:

- The below code is simple a set of print commands using strings

```
print("Hello and welcome to the user detail game")
print("Please enter your details below")
print("What is your first name?")
```
- The below code sets user inputs
```
first_name = input()
age = 29
print("What is your last name?")
last_name = input()
print("Hello" + " " + (first_name.capitalize()) + " " + (last_name.capitalize()))
```
- The below code uses conditional statements to allow to gather information from the user

```
print("Now" + " " + (first_name.capitalize()) + "," + " " + "I hear you are" +" " + (str(age)) + " " + "years of age, is that correct?")
answer = input("enter yes or no: ")
if answer == "yes":
    print("That's brilliant" + "," + "your name is" + " " + (first_name.capitalize()) + " " + "and you are" + " " + (
        str(age)) + " " + "years young!")

else:
    print("Oh dear!, my sincerest apologies. Let's get you back on track" + " " + (
        first_name).capitalize() + "." + " " + "How old are you?")
    age = int(input())
```

- The below code makes sure users can only enter an integer
```
print("Using digits, type your house number")
house_number = int(input())
print("What is the name of your road?")
road_name = input()
print("What Town do you live in?")
town_name = input()
print("and finally, your postcode please")
post_code = input()
```
- The below code uses further conditional rules to make sure the user is old enough to enter the programme

```
if age > 18:
    print("Thank you for all of that information" + " " + (first_name.capitalize()) + " " + (last_name[0].capitalize()) + "," + " " + "your age is " + str(age) + " and your address is" + " " + (house_number) + " " + (road_name.title()) + "," + " " + (town_name.title()) + "," + " " + (post_code.upper()) + ".")
else:
    print("Unfortunately you are underage, please come back in " + str(18-age) + " years.")
```


## **_Git ignore_**

This is used to keep files on your localhost to prevent it from being pushed up, git completely ignores files of this nature. Hence the name
Follow the below steps to accomplish creating a .gitignore file. 

(image)

(image)



# Definiton of Ready

- 100% manual recovery testing
- Age verified

# Definition of Done
- User acceptance testing
- Peer code reviews