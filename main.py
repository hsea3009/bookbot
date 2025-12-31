from stats import word_count,chars_dict_to_sorted_list, get_char_dict


def get_book_text(file_path):
  with open(file_path) as f:
    file_contexts = f.read()
    return file_contexts


def main(text):
  text = get_book_text("books/frankenstein.txt")
  chars_dict = get_chars_dict(text)               # <- pass text
  sorted_chars = chars_dict_to_sorted_list(chars_dict) 


if __name__ == "__main__":
  main(text)


# def sort_on(file_path):
#   with open(file_path) as f:
#     file_contexts = f.read()
#     letter_counts = {}
#     for char in file_contexts.lower():
#       if char.isalpha():
#         letter_counts[char] += 1
#   print(letter_counts)




  # book_text = get_book_text("books/frankenstein.txt")
  # print(book_text)
  # words = word_count("books/frankenstein.txt")
  # print(f'Found {words} total words')

  # text = text_count("books/frankenstein.txt")
  # print(text)

  # letter_count = sort_on("books/frankenstein.txt")
  # print(letter_count)
