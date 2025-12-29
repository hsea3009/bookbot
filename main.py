def get_book_text(file_path):
  with open(file_path) as f:
    file_contexts = f.read()
    return file_contexts

def main():
  get_book_text("books/frankenstein.txt")
  store = file_path
  print(file_path)

if __name__ == "__main__":
  main()
