import math
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, "." )+ "1$".rjust(4))
print("Muffin".ljust(16, "." )+ "2$".rjust(4))
print("Ice-cream".ljust(16, "." )+ "3$".rjust(4))


#indexing menu

print(title[0])


# some methods return boolean data
print(title.startswith("M"))
print(title.endswith("U"))

#boolean data
myValue = True
x = bool(False)
print(type(x))
print(isinstance(myValue, bool))

# numeric data type 
# int types

price = 100
base_price = int(150)
print(type(base_price))
print(isinstance(base_price, int))

#float type 
gpa = 3.8
y = float(1.8)

print(type(gpa))

#complex type

comp_value = 5 + 3j
print(comp_value)
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

#built in functions for numbers
abs(gpa)
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 0))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))


#casting a string into a number
zipcode = "10001"
zip_value = int(zipcode)
print(zip_value)

#if you try to cast a string into an integer it will not be possible




