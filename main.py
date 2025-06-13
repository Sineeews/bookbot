import sys
from stats import get_num_of_words, get_num_of_characters, get_sorted_characters

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text


def main():
    if len(sys.argv) == 2:
        print("============ BOOKBOT ============")
        print("Analyzing the book...")
        print("----------- Word Count ----------")
        print("")
        print(f"Found {get_num_of_words(get_book_text(sys.argv[1]))} total words")
        print("--------- Character Count -------")
        char_count = get_sorted_characters(get_num_of_characters(get_book_text(sys.argv[1])))
        for character in char_count:
            print(f"{character['char']}: {character['num']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
    
   