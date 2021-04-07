## You have rented some movies for your kids: 
## The little mermaid (for 3 days), 
## Brother Bear (for 5 days, they love it), and 
## Hercules (1 day, you don't know yet if they're going to like it). 
## If price for a movie per day is 3 dollars, how much will you have to pay?

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

Facebook = 350 * 10
Google = 400 * 6
Amazon = 380 * 4

weekly_pay = Facebook + Google + Amazon
weekly_pay
# output = 7420


