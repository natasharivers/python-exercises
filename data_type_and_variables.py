## You have rented some movies for your kids: 
## The little mermaid (for 3 days), 
## Brother Bear (for 5 days, they love it), and 
## Hercules (1 day, you don't know yet if they're going to like it). 
## If price for a movie per day is 3 dollars, how much will you have to pay?

little_mermaid = 3
brother_bear = 5
hercules = 1
price_per_day = 3
price_total = price_per_day *(little_mermaid + brother_bear + hercules)
print(price_total)

# PRACTICE DICTIONARY 
movie_one = {
    "movie" : "The Little Mermaid",
    "days" : 3,
    "favorability" : None,
    "price" : 3.00,
    "total_price" : 9.00
}

movie_two = {
    "movie" : "Brother Bear",
    "days" : 5,
    "favorability" : "loved",
    "price" : 3.00,
    "total_price" : 15.00
}

movie_three = {
    "movie" : "Hercules",
    "days" : 1,
    "favorability" : "unknown",
    "price" : 3.00,
    "total_price" : 3.00
}

movies_rented = [movie_one, movie_two, movie_three]
movies_rented


## Suppose you're working as a contractor for 3 companies: 
## Google, Amazon and Facebook, they pay you a different rate per hour. 
## Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
## How much will you receive in payment for this week? You worked 10 hours for Facebook, 
## 6 hours for Google and 4 hours for Amazon.

Facebook_pay = 350
Facebook_hrs = 10
Google_pay = 400
Google_hrs = 6
Amazon_pay= 380
Amazon_hrs = 4

weekly_pay = (Facebook_pay * Facebook_hrs) + (Google_pay * Google_hrs) + (Amazon_pay * Amazon_hrs)
weekly_pay
# output = 7420

## A student can be enrolled to a class only if the class is not full and 
## the class schedule does not conflict with her current schedule.
class_is_full = False
schedule_conflict = False
enrollable_status = not (class_is_full or schedule_conflict)
enrollable_status

## A product offer can be applied only if people buys more than 2 items, 
## and the offer has not expired. 
## Premium members do not need to buy a specific amount of products.


purchase_more_than_two = True
product_not_expired = True
premium_membership = False
discount_eligability = product_not_expired and (purchase_more_than_two or premium_membership)
discount_eligability


## NEXT SECTION- USERNAME/ PASSWORD## 
username = 'codeup'
password = 'notastrongpassword'
Create a variable that holds a boolean value for each of the following conditions:

#1- the password must be at least 5 characters
password_length = len(password) >= 5 
#2- the username must be no more than 20 characters
user_name_length = len(username) <= 20
#3- the password must not be the same as the username
qualification = password != username

user_and_password_valid = password_length and user_name_length and qualification

## BONUS neither the username or password can start or end with whitespace
#use "strip" function?
# no_white_space_username = not (username.startswith(' ') or username [-1] == ' ')
# no_white_space_password = not (password.startswith(' ') or password [-1] == ' ')
# user_and_password_valid = password_length and user_name_length and qualification and no_white_space_username and no_white_space_password 