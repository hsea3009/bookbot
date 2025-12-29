def get_book_text(file_path):
  with open(file_path) as f:
    file_contexts = f.read()
    return file_contexts

def word_count(file_path):
  with open(file_path) as f:
    file_contexts = f.read()
    words = file_contexts.split()
    return len(words)

def main():
  book_text = get_book_text("books/frankenstein.txt")
  print(book_text)
  words = word_count("books/frankenstein.txt")
  print(words)

  

if __name__ == "__main__":
  main()
