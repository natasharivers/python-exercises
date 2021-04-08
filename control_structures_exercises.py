# #1 Conditional Basics

#prompt the user for a day of the week, print out whether the day is Monday or not
day_of_week = input('what day of the week is it')
if day_of_week == 'Monday' or 'monday':
    print('Monday')
else:
    print ('Not Monday')

#prompt the user for a day of the week, print out whether the day is a weekday or a weekend
weekend_or_weekday = input('what day of the week is it')
if weekend_or_weekday == 'Monday':
    print('weekday')
elif weekend_or_weekday == 'Tuesday' or 'tuesday':
    print('weekday')
elif weekend_or_weekday == 'Wednesday' or 'wednesday':
    print('weekday')
elif weekend_or_weekday == 'Thursday' or 'thursday':
    print('weekday')
elif weekend_or_weekday == 'Friday' or 'friday':
    print('weekday')
else:
    print ('weekend')

#create variables and make up values for

#the number of hours worked in one week
hours_per_day = 8
days_per_week = 5
hours_per_week = hours_per_day * days_per_week
hours_per_week = 40

#the hourly rate
hourly_rate = 40

#how much the week's paycheck will be
hourly_rate = 40
overtime_pay = 1.5 * hourly_rate
weekly_pay = (hours_per_week * hourly_rate) + overtime_pay

#write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

hours_worked = input('how many hours did you work')
h= float(hours_worked)
hourly_pay = 40

if h <= 40:
    pay = h*hourly_pay
elif h > 40:
    pay = ((h-40)*hourly_pay*1.5)+hourly_pay*40   

print ("Your weekly paycheck is %.2f" %pay)

# #2 Loop Basics

##2A  WHILE LOOPS

#Create an integer variable i with a value of 5.
i = 5

#Create a while loop that runs so long as i is less than or equal to 15
i = 5
while i <= 15:
    print(i)
  
#Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i += 1

#Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while i <= 100:
    print(i)
    i += 2

#Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i += -5

#Create a while loop that starts at 2, 
#and displays the number squared on each line while the number is less than 1,000,000.
i = 2
while i < 1000000:
    print(i)
    i **= 2
 

# Write a loop that uses print to create the output shown below.
i = 100
while i >= 5:
    print(i)
    i += -5

##2B FOR LOOPS
#i Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
multiply_by = int(input("enter desired number"))
for i in range(1,11):
    print(multiply_by, 'x', i, '=', multiply_by*i)

#ii Create a for loop that uses print to create the output shown below.
for i in range(1,11):
    for j in range (1, i+1):
        print(i, end="")
    print()

#2C BREAK AND CONTINUE
## i Prompt the user for an odd number between 1 and 50. 
#Use a loop and a break statement to continue prompting the user if they enter invalid input. 
#(Hint: use the isdigit method on strings to determine this). 
#Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
#except for the number the user entered.
while True:
    odd_num = input('Enter odd number between 1 and 50:')
    if odd_num.isdigit() and int(odd_num) % 2 == 1 and int(odd_num) <= 50:
            break
 odd_num = int(odd_num)
for num in range(1, 50, 2):
    if num == odd_num:
        print('Yikes! Skipping number: ', num)
    else:
        print('Here is an odd number: ', num)
## KEEP TRYING TO FIGURE IT OUT- MADELINE INSTRUCTION ^^^^       

#2D 
while True:
    odd_num = input('Enter odd number between 1 and 50:')
    if odd_num.isdigit(): 
        if int(odd_num) > 0:
            break
odd_num = int(odd_num)
for num in range (0, odd_num +1):
    print(num)


#2E Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.
while True:
    odd_num = input('Enter odd number between 1 and 50:')
    if odd_num.isdigit():
        if int(odd_num) > 0:
            break


##3 Fizzbuzz One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
#Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

#Write a program that prints the numbers from 1 to 100.
for i in range(1,101): 
		print(i) 

#For multiples of three print "Fizz" instead of the number
for num in range(1, 101):
    if num % 3 == 0:
        print('Fizz')
    else:
        print(num)

#For the multiples of five print "Buzz".
for num in range(1, 101):
    if num % 5 == 0:
        print('Buzz')
    else:
        print(num)

#For numbers which are multiples of both three and five print "FizzBuzz".
for num in range(1, 101):
    if num % 3 == 0:
        print('Fizz')
    if num % 5 == 0:
        print('Buzz')
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    else:
        print(num)

#found online -second way of completing
for num in range(1,101):
    string = ""
    if num % 5 == 0:
        string = string + "Buzz"
    if num % 3 == 0:
        string = string + "Fizz"
    elif num % 5 != 0 and num % 3 != 0 :
        string = string + str(num)
    print(string)
##4 Display a table of powers.

#Prompt the user to enter an integer.
integer = int(input("what number would you like to go up to"))

#Display a table of squares and cubes from 1 to the value entered.
integer = int(input("what number would you like to go up to?"))
print("number       squared     cubed  ")
print("---------    ---------   --------")

for i in range(integer):
    print(i,"\t", "\t", squared(i), "\t", "\t", cubed(i))

#Ask if the user wants to continue.
#Assume that the user will enter valid data.
#Only continue if the user agrees to.

while True:
    posited_num = input('Please insert a positive integer:')
    if posited_num.isdigit():
        if int(posited_num) >0:
            break
proceed = input('do you want to proceed?: ')
if proceed.lower().startwith('y'):
    posited_num = int(posited_num)
    print()
    print('number | squared | cubed')
    print('------ | ------- | -----')
    for i in range(1, posited_num + 1):
        i_squared = i ** 2
        i_cubed = i ** 3
        print(f'{i: 6} | {i_squared: 7} | {i_cubed: 5}')

#5 Convert given number grades into letter grades.
while True:
    user_number = input('input the grade')
    if user_number.isdigit():
        user_number = int(user_number)
        if user_number < 0 or user_number > 100:
            continue
        break
if grade in range(60):
    grade = 'F'
elif grade in range(60, 67):
    grade = 'D'
elif grade in range(67, 80):
    grade = 'C'
elif grade in range(80, 88):
    grade = 'B'
else:
    grade = 'A'

bookshelf = [
    {'title': 'ABC',
    'author' : 'moon',
    'genre': 'kids'},
    {'title': 'dogs',
    'author' : 'boxer',
    'genre': 'veternary'}
    {'title': 'favorite candy',
    'author' : 'dr suess',
    'genre': 'children'}]

for book in bookshelf:
    [print(key, ': ', book[key]) for key in book]
    print('--------')

