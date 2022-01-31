#  Kids drink toddy.
# Teens drink coke.
# Young adults drink beer.
# Adults drink whisky.
# Make a function that receive age, and return what they drink.
# Rules:-
# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.

def drink(age):
    if age<14:
        return "toddy"
    elif age<18:
        return "coke"
    elif age<21:
        return "beer"
    elif age>=21:
        return "Whisky"
age=int(input("Enter any age:-"))
print(drink(age))