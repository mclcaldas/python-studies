#1. Write a program that reads an integer and prints it.

int_number = input('Enter a int number: ')
print ('Number: ', int_number)

#2. Write a program that asks the user to enter three integer values ​​and print their sum.

print('Enter three integer values for sum')
number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))
number3 = int(input("Enter Third Number: "))

result = number1 + number2 + number3

print("Result:", result)

#3. Write a program that receives three values ​​and presents the sum of the squares of the values ​​read.

print("Enter three values: ")
number1 = float(input("Enter First Number: "))
number2 = float(input("Enter Second Number: "))
number3 = float(input("Enter Third Number: "))

result_square = (number1 ** 2) + (number2 ** 2) + (number3 ** 2)

print("Result of the sum of the squares of the values: ", result_square)