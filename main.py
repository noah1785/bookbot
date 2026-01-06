from stats import get_book_text, word_count, char, sort_dict

#def main():
#    txt = get_book_text('books/frankenstein.txt')
#    print(txt)

path_to_file = 'books/frankenstein.txt'

num_words = word_count(path_to_file)

sorted = sort_dict(char(path_to_file))

#print(char(path_to_file))
print("============ BOOKBOT ============")
print(f"Analyzing book found at {path_to_file}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")
for i in sorted:
    dict = i
    print(f"{dict['name']}: {dict['num']}")
print("============= END ===============")