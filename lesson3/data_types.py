# String data type 

#literal Assignment
# first = "Joe"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))


#Constructor assignment
# pizza = str("Pepporoni")
# print(type(pizza))
# print(type(pizza)==str)
# print(isinstance(pizza, str))

# Concatenation

# first_name = "Joseph"
# second_name = "Otundo"
# full_Name = first_name + " " + second_name
# full_Name += "!!"
# print(full_Name)

# #Python type Casting
# decade = str(1980)
# print(type(decade))
# print(isinstance(decade, str))

# statement = "I like music from the " + decade + "s"
# print(statement)

#Multilines
# multilines = '''

# hey how are you 
#         I was just checking in

#     all good?😂😂❤️❤️😍

#                 '''
# print(multilines)

#escaping special characters

sentence = "I\'m back at work! \t Hey! \n\n where\'s this at \\located"

#string methods
# print(sentence.lower())
# print(sentence.upper())
# print(sentence )
# print(sentence.title())
# print(sentence.replace("work", "Job"))
sentence += "                                                                   "

print(len(sentence))
print(len(sentence.lstrip()))
print(len(sentence.rstrip()))
print(len(sentence.strip()))







