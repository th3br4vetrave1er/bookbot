def reader(path_to_book="/home/br4vetrave1er/workspace/bookbot/books/Romeo_and_Juliet.txt"):
  with open(path_to_book) as book:
    return book.read()

print(reader())