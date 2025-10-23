def get_book_text(text):
    with open(text) as w:
            file_contents = w.read()
            return file_contents

def char_count():
      file_contents=get_book_text("books/frankenstein.txt")
      lower_chars=file_contents.lower()
      char_count={}
      for i in lower_chars:
            if i in char_count:
                  char_count[i]+=1
            else:
                char_count[i]=1
        return char_count
            


     
