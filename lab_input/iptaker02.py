#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - concatenate vs print a series of items"""

def main():

    # collect string input from the user
    user_input = input("Please enter an IPv4 IP address:")
    
    ## the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is: " + user_input)
    
    ## print() can be given a series of objects separated by a comma
    print("You told me the IPv4 address is:", user_input)

    # this line collects and store input
    user_vendor = input("Please enter your device vendor:")

    # this will print 
    print("The vendor's name is ", user_vendor)

main()
