def main():
    book_path = input("Enter your book path: ")
    text = file_path(book_path)
    words = word_counter(text)
    characters = dict(sorted(char_dict(text).items(), key=lambda item: item[1], reverse=True))
    #sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    #создаёт отсортированный список пар (ключ, значение), сортируя по значению (item[1]) в порядке убывания (reverse=True).
    #print(text)
    #print(characters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    for keys, value in characters.items():
        print(f"The '{keys}' character was found {value} times")
    print("--- End report ---")


def file_path(path):
    with open(path) as book:
        return book.read()

def word_counter(book):
    return len(book.split())

def char_dict(source):
    import string
    char_dict = dict.fromkeys(string.ascii_lowercase, 0)
    for i in source.lower():
        if i in char_dict:
            char_dict[i] += 1
    return char_dict


main()