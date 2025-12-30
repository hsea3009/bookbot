from stats import word_count, text_count, sort_on

def get_book_text(file_path):
  with open(file_path) as f:
    file_contexts = f.read()
    return file_contexts


def main():
  book_text = get_book_text("books/frankenstein.txt")
  print(book_text)
  words = word_count("books/frankenstein.txt")
  print(f'Found {words} total words')

  text = text_count("books/frankenstein.txt")
  print(text)

  letter_count = sort_on("books/frankenstein.txt")
  print(letter_count)

if __name__ == "__main__":
  main()


# def sort_on(file_path):
#   with open(file_path) as f:
#     file_contexts = f.read()
#     letter_counts = {}
#     for char in file_contexts.lower():
#       if char.isalpha():
#         letter_counts[char] += 1
#   print(letter_counts)
