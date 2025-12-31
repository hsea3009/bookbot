def word_count(file_path):
  with open(file_path) as f:
    file_contexts = f.read()
    words = file_contexts.split()
    return len(words)

def text_count(file_path):
  p_count = 0
  t_count = 0
  c_count = 0
  with open(file_path) as f:
    file_contexts = f.read()
    for letter in file_contexts:
      if letter.lower() == "p":
        p_count += 1
      if letter.lower() == "t":
        t_count += 1
      if letter.lower() == "c":
        c_count += 1
  print(f"'t': {t_count}, 'p': {p_count}, 'c': {c_count}")


def get_char_dict(text):
    letter_counts = {}
    for char in text.lower():
      if char.isalpha():
        if char in letter_counts:
          letter_counts[char] += 1
        else:
          letter_counts[char] = 1
    return letter_counts

def chars_dict_to_sorted_list(chars_dict):
    list_of_dict = []
    for char, num in chars_dict.items():
        entry = {"char": char, "num": num}
        list_of_dict.append(entry)

    def sort_on_num(item):
        return item["num"]

    list_of_dict.sort(reverse=True, key=sort_on_num)
    return list_of_dict
