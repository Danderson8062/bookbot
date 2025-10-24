from stats import get_book_text, word_count, char_count, sort_on, get_sorted_char_list
book_path="books/frankenstein.txt"
text=get_book_text("books/frankenstein.txt")
num_words=word_count(text)
num_chars=char_count(text)
num_chars_sorted=get_sorted_char_list(num_chars)
print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")
for item in num_chars_sorted:
    ch = item["char"]
    if not ch.isalpha():
        continue
    print(f"{ch}: {item['num']}")
print("============= END ===============")