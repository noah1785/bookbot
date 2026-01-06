def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    txt = get_book_text('c:/Users/noahg/workspace/github.com/noah1785/bookbot/books/frankenstein.txt')
    print(txt)

main()