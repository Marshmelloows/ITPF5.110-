#book options
import time
#i am importing time so that i can allow my my text to be printed at a set rate that i choose insted of evreything all at once

#all of the book options that are avalible to read

book_options = ("Alice (1)",
                "Blue eyes (2)",
                "OLD WORLD (3)",
                "The care of the skin and hair (4)",
                "Hiddin Seed(5)",
                "A summer journey to Brazil(6)",
                "Wee Johnnie Paterson, & other humorous sketches(7)",
                "Return to Earth (8)",
                "celebs (9)",
                "Die (10)")       


#slow print function
#this function prints text one character at a time with a delay
#changing the delay will work as such. makign the float number bigger will make the print slower adn making smaller will make it print faster
def slow_print(text: str, delay: float = 0.01): 
    """Prints text one character at a time with a delay."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Print a newline at the end


#filename = f"{title}.txt"
#prints books in list in a nice format
def ChooseBook():
    print("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
    print("|          Avalible books        |")
    print("|{==============================}|")
    for book in book_options :
       print(f"|   | {book:<27}|")#this part of
    print("|{==============================}|")
    print("|       please pick one of       |")
    print("|           thease books         |")
    print("L________________________________j")
    #waits so that the reader can atuley read the list 
    time.sleep(2)

#grabs the book that is requested and changes the book so that 
def getting_book():
    while True:
        try:    
            numberinput = int(input("enter book number"))

            if numberinput ==0:
                print("goodbye")
                exit()
            elif numberinput >= 1 and numberinput <= len(book_options):
            #if 1 <= numberinput <= len(book_options):
                return numberinput
            else:
                print(f"Invalid number")
        except ValueError:
            print("that is not number")


        
# here choice is already = to the book name from the list
# instead of creating new variables we just use the choice argument which contains the book name to read out the file
def Read_books(choice):
    if choice == 1:
        f = open("Alice.txt", encoding = "UTF-8")
    elif choice == 2:
       #this was used to debug print("hi")
        f = open("Blue eyes.txt", encoding = "UTF-8")
    elif choice == 3:
       # used to debug print("hi")
        f = open("OLD WORLD.txt", encoding = "UTF-8")
    elif choice == 4:
        f = open("Lotion on its skin.txt", encoding = "UTF-8")
    elif choice == 5:
        f = open("Hidden Seed.txt", encoding = "UTF-8")
    elif choice == 6:
        f = open("Brazil.txt", encoding = "UTF-8") 
    elif choice == 7:
        f = open("Humorous.txt", encoding = "UTF-8")
    elif choice == 8:
        f = open("Return to Earth.txt", encoding = "UTF-8")
    elif choice == 9:
        f = open("celebes.txt", encoding = "UTF-8")
    elif choice == 10:
        f = open("Die.txt", encoding = "UTF-8")


    for line in f:
        slow_print(line, 0.02)
    
    
#main loop
while True:
    ChooseBook()
    choice = getting_book()
    if choice is None:
        break
    #selected_book = book_options[choice -1]
    Read_books(choice)
    #Read_books(choice)
    print(choice)