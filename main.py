path_to_book = "books/frankenstein.txt"

def main():
    path = path_to_book()
    with open(path) as book:
        print(book.read(), word_counter())
        
    
def path_to_book(a="books/frankenstein.txt"):
    your_path = input("Enter path to book: ")
    return your_path


def word_counter(path="books/frankenstein.txt"):
    words = main()
    return len(words.split())



main()