# number = int(input("Input a number to check if its odd or even: "))

# if number % 2 == 0:
#     print("this is an even number")
# elif number % 2 > 0:
#     print("this is an odd number")

# leapyear

input_year = int(
    input("To check if a given year is a leap year, input the year here :"))

if input_year % 4 != 0:
    print("this is not a leap year")
elif input_year % 100 == 0 and input_year % 400 == 0:
    print("this is a leap year")
elif input_year % 100 == 0 and input_year % 400 != 0:
    print("This is not a leap year")
elif input_year % 100 != 0:
    print("This is a leap year")
