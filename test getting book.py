



#grabs the book that is requested
def getting_book():
    book_options = ("1:alice", "2:gweto", "3:sputnic","4:is", "5:the book of the dead", "6:the book of the living", "7:the book of the dead 2", "8:the book of the living 2", "9:the book of the dead 3", "10:the book of the living 3")
    books = int (input("what book?:"))[books -1]
    your_book = book_options[books]
    print({your_book})



books =[]
book_options = ("1:alice", "2:gweto", "3:sputnic","4:is", "5:the book of the dead", "6:the book of the living", "7:the book of the dead 2", "8:the book of the living 2", "9:the book of the dead 3", "10:the book of the living 3")
 
def new_gettingbook():
    is_your_book = int(input("enter your book!!:"))
    book = book_options[is_your_book -1]
    print(f"you have picked:{book}")
    books.append(book)
    return book

new_gettingbook()
