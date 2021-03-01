import math

precision = int(input("Add a number "))

while precision > 50:
	print("Number to large")
	precision = int(raw_input("How many spaces? "))
else:
	print('%.*f' % (precision, math.pi))


