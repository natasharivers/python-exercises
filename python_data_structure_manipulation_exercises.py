# #1 How many students are there?
len(students)

# #2 How many students prefer light coffee? 
# For each type of coffee roast?
print(students[0]["coffee_preference"])

prefer_light = []
for student in students:
    if student["coffee_preference"] == "light":
        prefer_light.append(student)
    else:
        continue
    print(len(prefer_light))