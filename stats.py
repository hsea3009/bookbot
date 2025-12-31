
def word_count(text):
    words = text.split()
    return len(words)


def get_char_dict(text):
    letter_counts = {}
    for char in text.lower():
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts


def sort_on(item):
    return item["num"]


def chars_dict_to_sorted_list(chars_dict):
    list_of_dict = []
    for char, num in chars_dict.items():
        entry = {"char": char, "num": num}
        list_of_dict.append(entry)

    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict
