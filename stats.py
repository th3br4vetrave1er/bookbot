def word_counter(text) -> int:
    """Count words in text and return the number as an integer"""
    return len(text.split())


def char_counter(text) -> int:
    counter_dict = {}
    for char in text.lower():
        if char in counter_dict:
            counter_dict[char] += 1
        else:
            counter_dict[char] = 1
    return counter_dict


def sort_chars(char_dict):
    # Convert the dictionary to a list of dictionaries
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})

    # Sort the list by count in descending order
    chars_list.sort(reverse=True, key=lambda x: x["count"])

    return chars_list
