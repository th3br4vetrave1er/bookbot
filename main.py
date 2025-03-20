import sys
from stats import word_counter, char_counter, sort_chars

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

PATH = sys.argv[1]  # The book path is the second argument


def get_book_text(path) -> str:
    with open(path) as f:
        text = f.read()
        return text


def bookbot_func(path, word_count, sorted_chars):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}')  # Using the passed path parameter
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f'{char}: {count}')
    print('============= END ===============')


def main():
    text = get_book_text(PATH)
    word_count = word_counter(text)
    char_dict = char_counter(text)
    sorted_chars = sort_chars(char_dict)

    bookbot_func(path=PATH, word_count=word_count, sorted_chars=sorted_chars)


if __name__ == '__main__':
    main()