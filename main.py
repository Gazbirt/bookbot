from stats import num_of_words
from stats import char_count
from stats import dictionary_sort
import sys

def get_book_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_contents = get_book_text(sys.argv[1])
    count = num_of_words(file_contents)
    
    char_dict = char_count(file_contents)

    sortedList = dictionary_sort(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for letter in sortedList:
        if letter[0].isalpha():
            print(f"{letter[0]}: {letter[1]}")
    print("============= END ===============")


main()
