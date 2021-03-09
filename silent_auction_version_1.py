from replit import clear
"""
This silent auction program allows users to bid without knowing what others bid.
This program utilizes a dictionary to store user names and their bids.
Version 1.0 
- Line 35 Need to make check when user doesn't enter 'yes' or 'no'.
- Need to make check when two users have the same bids. 

"""
#HINT: You can call clear() to clear the output in the console.

#Create new dictionary to store bidders and their bids.
bidders = {}

#Adds the bidder and their bids to a dictionary.
def add_bidder(bidder, price):
    bidders[bidder] = price 

#Welcome user.
print("Welcome to the Secret Auction!")

#Loop thru until there are no more bidders
other_bidders = True
while other_bidders == True:
    #Ask user for name and bid.
    bidder_name = input("Type in your name: ")
    bidder_price= int(input("Type in your bid: $ "))

    #Store the data in a dictionary.
    add_bidder(bidder_name, bidder_price)

    #Clear the screen.
    clear()

    #Ask if there are any other bidders 
    new_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")

    #Get out of loop if user says no
    if new_bidders == 'no':
        other_bidders = False
#DEBUG 
print(bidders)

#Check the dictionary key value pairs with the highest bid.
highest_bid = 0
highest_bidder = ''
for key in bidders:
    if int(bidders[key]) > highest_bid:
        highest_bidder = key
        highest_bid = bidders[key]

#DEBUG
#print("Highest bid = " + str(highest_bid))
#print("Highest bidder = " + bidders[highest_bid])

#Print the highest bidder and their bid 
print("The winner is " + highest_bidder + " with a bid of $" + str(highest_bid))
