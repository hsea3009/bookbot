def word_count(file_path):
  with open(file_path) as f:
    file_contexts = f.read()
    words = file_contexts.split()
    return len(words)
