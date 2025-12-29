def get_book_text(file_path):
  with open(file_path) as f:
    file_contexts = f.read()
    return file_contexts

def main():
  book_text = get_book_text("books/frankenstein.txt")
  print(book_text)

if __name__ == "__main__":
  main()
