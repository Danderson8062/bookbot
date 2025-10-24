def get_book_text(text):
    with open(text) as w:
            file_contents = w.read()
            return file_contents

def word_count(file_contents):
      words=file_contents.split()
      word_count=len(words)
      return word_count


def char_count(file_contents):
      lower_chars=file_contents.lower()
      chars_count={}
      for i in lower_chars:
            if i in chars_count:
                  chars_count[i]+=1
            else:
                chars_count[i]=1
      return chars_count


def sort_on(items):
     return items["num"]

def get_sorted_char_list(char_counts):
      results_list = []
      for char, count in char_counts.items():
            if not char.isalpha():
                  continue
            results_list.append({"char": char, "num": count})
      results_list.sort(reverse=True, key=sort_on)
      return results_list