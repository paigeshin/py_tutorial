import math 

def paint_calc(height, width, cover):
    area = height * width 
    number_of_cans = math.ceil(area / cover)
    print(f"You'll need {number_of_cans} cans of paint")