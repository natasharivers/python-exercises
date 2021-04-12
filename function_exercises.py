# 1 Define a function named is_two. It should accept one input and 
# return True if the passed input is either the number or the string 2, False otherwise.

#accepts one input, retunrs true if its 2 or '2'
#otherwise return false

def is_two(number):
    """
    return true to a input if it's 2 number or 2 string
    return False is any other number or string
    """
    if number == 2:
        return True
    if number == '2':
        return True
    else:
        return False

#2 Define a function named is_vowel. It should return True 
# if the passed string is a vowel, False otherwise.

def is_vowel(vowelstring):
    """
    return true if input is upper or lowercase vowel
    return False if input is consonant
    """
    if vowelstring == ('a' or 'e' or 'i' or 'o' or 'u'):
        return True
    if vowelstring == ('A' or 'E' or 'I' or 'O' or 'U'):
        return True
    else:
        return False

#3 Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.

def is_consonant(constrng):
    """
    return true if input is a consonant 
    return False if input is a vowel
    """
    if constrng in ('a' or 'e' or 'i' or 'o' or 'u'):
        return False
    if constrng in ('A' or 'E' or 'I' or 'O' or 'U'):
        return False
    else:
        return True

#HAPPY PATH#
def is_consonant(string):
    if type(string) == str:
        is_only_letters = string.isalpha()
        return is_only_letters and not is_vowel(string)
    else:
        return False

#4 Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.

def cap_first_cons(string):
    """
    capitalizes word if it begins with a consonant 
    """
    if string[0] in ('a' or 'e' or 'i' or 'o' or 'u'):
        return ("invalid")
    else:
        return string.capitalize()
print(cap_first_cons("dog"))

#OR

def cap_first_cons(string):
    if type(string) != str:
        return False
    
    first_letter = string[0] 
    if is_consonant(first_letter):
        string = string.capitalize()

    return string

#5 Define a function named calculate_tip. 
# It should accept a tip percentage (a number between 0 and 1) and the bill total, 
# and return the amount to tip.

def calculate_tip(bill =1, tip =2 ):
    return bill * tip
calculate_tip(100, .5)

#6 Define a function named apply_discount. 
# It should accept a original price, and a discount percentage, 
# and return the price after the discount is applied.

def apply_discount(price =1, discount =2 ):
    return price - ((discount / 100) * price)
apply_discount(100, 20)

#7 Define a function named handle_commas. 
# It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(string):
    string = string.replace("," , "") 
    return string

#CORRECTED (below)

def handle_commas(string):
    if type(string) != str:
        return "Input must be a string"
    
    return float(string.replace("," , ""))

#8 Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).

def is_letter_grade(score):
    if(score < 60):
        return "F"
    elif(score < 70):
        return "D"
    elif(score < 80):
        return "C"
    elif(score < 90):
        return "B"
    elif(score <101):
        return "A"
        
#ALSO CORRECT BUT WITH TYPE AS INT OR FLOAT

def is_letter_grade(score):
    if type(grade) == int or type(grade) == float:    
        if(score < 60):
            return "F"
        elif(score < 70):
            return "D"
        elif(score < 80):
            return "C"
        elif(score < 90):
            return "B"
        elif(score <101):
            return "A"

#9 Define a function named remove_vowels that accepts a string and 
# returns a string with all the vowels removed.

def remove_vowels(string):
    vowels = ('a', 'e', 'i', 'o', 'u') 
    for x in string.lower():
        if x in vowels:
            string = string.replace(x, "")
              
    print(string)



#10 Define a function named normalize_name. 
# It should accept a string and return a valid python identifier, that is:
#anything that is not a valid python identifier should be removed
#leading and trailing whitespace should be removed
#everything should be lowercase
#spaces should be replaced with underscores

def normalize_name(string):
    string = string.replace("$", "")
    string = string.replace("%", "")
    string = string.replace("!", "")
    string = string.replace(" ", "_")
    string = string.lower()
    return(string)

#11 Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.





