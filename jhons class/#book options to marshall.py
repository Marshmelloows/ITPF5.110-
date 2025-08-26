#book options
import time
#i am importing time so that i can allow my my text to be printed at a set rate that i choose insted of evreything all at once

import sys
book_options = ("1:alice", "2:gweto", "3:sputnic","4:is", "5:the book of the dead", "6:the book of the living", "7:the book of the dead 2", "8:the book of the living 2", "9:the book of the dead 3", "10:the book of the living 3")



#slow print function
#this function prints text one character at a time with a delay
#changing the delay will work as such. makign the float number bigger will make the print slower adn making smaller will make it print faster
def slow_print(text: str, delay: float = 0.01): 
    """Prints text one character at a time with a delay."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Print a newline at the end



#prints books in list in a nice format
def ChooseBook():
    print("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
    print("|          Avalible books        |")
    print("|{==============================}|")
    for book in book_options :
       slow_print(f"|   | {book:<27}|")#this part of
    print("|{==============================}|")
    print("|       please pick one of       |")
    print("|           thease books         |")
    print("L________________________________j")
    #waits so that the reader can atuley read the list 
    time.sleep(2)

#grabs the book that is requested and changes the book so that 
def getting_book():
    book_number = int(input("please put down a number for what book you want:"))
    if 1 <= book_number <= len(book_options):
        book = book_options[book_number - 1]
        print(f"you have selected: {book}")
        time.sleep(2)
        return book
    else:
        print("Invalid book number please try again")
        getting_book()
        

def reading_book():
    if book_options == 1:
        print ("this is allise")
    elif book_options == 2:
        print ("this is gweto")
    elif book_options == 3:
        print ("this is sputnic")
    elif book_options == 4:
        print ("this is is")
    elif book_options == 5:
        print ("this is the book of the dead")
    elif book_options == 6:
        print ("this is he book of the living")
    elif book_options == 7:
        print ("this is the book of the dead 2")
    elif book_options == 8:
        print ("this is the book of the living 2")
    elif book_options == 9:
        print ("this is the book of the dead 3")
    elif book_options == 10:
        print ("this is the book of the living 3")
    else:
        print("this is not a book")
    
#main loop
while True:
    ChooseBook()
    getting_book()
    reading_book()
    