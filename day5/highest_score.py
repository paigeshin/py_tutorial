student_scores = input("Input a list of student heights without ',' or empty space. ex) 99 66 88 ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# print(min(student_scores))
# print(max(student_scores))

highest_score = 0 
for score in student_scores:
    if score > highest_score:
        highest_score = score 
print(f"The highest score in the class is: {highest_score}")