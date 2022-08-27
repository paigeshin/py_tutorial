# Type Error 
num_char = len(input("What is your name?"))
# print("Your name has " + num_char + " characters.")

print(type(num_char) ) # class 'int'

# Solve Type Error 
new_num_char = str(num_char)
print("Your name has " + new_num_char +  " characters.") 