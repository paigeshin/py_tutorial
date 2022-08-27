print(8 / 3) # 2.66666665 
print(int(8 / 3)) # 2 

# round 
print(round(8 / 3)) # 3 

# round by specifying number of digits 
print(round(8 / 3, 2)) # 2.67 

# devision for whole number   
print(8 // 3) # 2 
print(type(8 // 3)) # class 'int'

# devision by default is floating number 
print(type(8 / 4))  # class 'float

# normal way for deivsion 
result = 4 / 2  
print(result) # 2.0 

# shortened version for operators 
result /= 2 
print(result) # 1.0 

# shortened version for operators 
score = 2 
score *= 2 
score += 2 
score -= 2 
score /= 2 

# f-String 
score = 0 
height = 1.8 
isWinning = True 
#f-String 
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")