#är du här ludwig?
import sys
import math

#starting message
print("hej denna räknare är lika dålig som en 7 åring")

#get user input
number1 = input("Skriv första termen: ")
symbol = input("Skriv räknesätt +, -, *, /, ^, } : ")
if symbol != "}":
	number2 = input("Skriv andra termen: ")

#calculate
def calc():
	if symbol == "+":
		print(float(number1) + float(number2))
	elif symbol == "-":
		print(float(number1) - float(number2))
	elif symbol == "*":
		print(float(number1) * float(number2))
	elif symbol == "/":
		print(float(number1) / float(number2))
	elif symbol == "^":
		print(float(number1)**float(number2))
	elif symbol == "}":
		print(math.sqrt(float(number1)))
	else:
		print("Du skrev ej en giltig symbol!")


calc()
