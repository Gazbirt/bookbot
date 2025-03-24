from stats import num_of_words
from stats import char_count

def get_book_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
    return file_contents


def main():
    file_contents = get_book_text("books/frankenstein.txt")
    count = num_of_words(file_contents)
    print(f"{count} words found in the document")

    char_dict = char_count(file_contents)
    print(char_dict)


main()
