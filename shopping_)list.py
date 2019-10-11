#-------------------------------------------------------------------------------
# Name:        Shoppping List
# Purpose:
#
# Author:      kenny.coons
#
# Created:     11/10/2019
# Copyright:   (c) kenny.coons 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Imports
import time

#-----------------Shopping List/Dictionary-----------
shopping_list = {}

#Functions----------
def add_items():
    stop = False
    while stop == False:
        items = input("what do you want to add to your shopping list").lower()
        if items == "stop":
            stop = True
        elif items != "stop":
            value = input("how much of that would you like to add")
            print ("adding", value, items)
            shopping_list[items] = value

def remove_items():
    stop = False
    while stop == False:
        items = input("what would you like to remove from your list").lower()
    if items == "stop":
        stop = True
    elif items != "stop":
        if items in shopping_list:
            print ("removing", items)
            del shopping_list[items]


def view_items():
    stop = False
    for(items, value) in shopping_list.items():
        print ("You have", value, items, "in your list")

def stop_stuff():
    stop = True

def main():
    play = 1
    print("Time to go shopping")
    while play == 1:
        time.sleep(1)
        choice = input("Would you like to add or remove items, view the list or stop?").lower()
        if choice == "add":
            add_items()
        elif choice == "remove":
            remove_items()
        elif choice == "view":
            view_items()
        elif choice == "stop":
            stop_stuff()
            play = 0
            print("You have finished your list")
            view_items()
        else:
            print("i am sorry, i didn't understand that")

#Main Code#
main()

