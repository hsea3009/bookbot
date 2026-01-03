from stats import word_count,chars_dict_to_sorted_list, get_char_dict
import sys

def get_book_text(file_path):
  with open(file_path) as f:
    file_contexts = f.read()
    return file_contexts


def main():
  text = get_book_text("books/*")
  num_words = word_count(text)
  chars_dict = get_char_dict(text)               
  sorted_chars = chars_dict_to_sorted_list(chars_dict)

  for item in sorted_chars:
    ch = item["char"]
    if not ch.isalpha():
      continue
    print(f"{ch}: {item['num']}")

if __name__ == "__main__":
  main()

print(sys.argv)


print(sys.argv[0])

print(sys.argv[0])



# from stats import word_count, chars_dict_to_sorted_list, get_char_dict


# def get_book_text(file_path):
#     with open(file_path) as f:
#         return f.read()


# def main():
#     text = get_book_text("books/frankenstein.txt")

#     # word count
#     num_words = word_count(text)
#     print("============ BOOKBOT ============")
#     print("Analyzing book found at books/frankenstein.txt...")
#     print("----------- Word Count ----------")
#     print(f"Found {num_words} total words")
#     print("--------- Character Count -------")

#     # char counts
#     chars_dict = get_char_dict(text)
#     sorted_chars = chars_dict_to_sorted_list(chars_dict)

#     for item in sorted_chars:
#         ch = item["char"]
#         if not ch.isalpha():
#             continue
#         print(f"{ch}: {item['num']}")
#     print("============= END ===============")


# if __name__ == "__main__":
#     main()
