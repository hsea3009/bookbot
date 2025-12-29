def main():
  def get_book_text():
    with open("books/frankenstein.txt") as f:
      file_contexts = f.read()
      print(file_contexts)

if __name__ == "__main__":
  main()
