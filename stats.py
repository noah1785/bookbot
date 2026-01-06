def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def word_count(path_to_file):
    txt = get_book_text(path_to_file)
    words = txt.split()
    num_o_words = len(words)
    return num_o_words

def char(path_to_file):
    characters = []
    txt = get_book_text(path_to_file)
    char_counts = {}

    for char in txt.lower():
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    list = []
    for i in dict:
        subdict = {}
        subdict['name'] = i
        subdict['num'] = dict[i]
        list.append(subdict)
    list.sort(reverse=True, key=sort_on)
    return list
