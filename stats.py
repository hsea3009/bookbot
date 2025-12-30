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


def sort_on(file_path):
  with open(file_path) as f:
    file_contexts = f.read()
    letter_counts = {}
    for char in file_contexts.lower():
      if char.isalpha():
        letter_counts[char] += 1
  print(letter_counts)
