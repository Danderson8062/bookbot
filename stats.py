def get_book_text(text):
    with open(text) as w:
            file_contents = w.read()
            return file_contents

def word_count():
      file_contents = get_book_text("books/frankenstein.txt")
      words=file_contents.split()
      word_count=len(words)
      print(f"Found {word_count} total words")

word_count()