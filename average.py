# Author: Samuel Bennett
# Date: 4/6/2021
# Description: Prints the average of five input numbers with prompts and final message with result

print("This program gives the average of five numbers.")
number_1 = float(input("Please enter first number: "))
number_2 = float(input("Please enter second number: "))
number_3 = float(input("Please enter third number: "))
number_4 = float(input("Please enter fourth number: "))
number_5 = float(input("Please enter fifth number: "))

totalAmountOfNumbers = 5

average = (number_1 + number_2 + number_3 + number_4 + number_5) / totalAmountOfNumbers

print ("The average of those numbers is: ", average)