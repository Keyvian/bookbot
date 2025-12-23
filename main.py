import sys
from stats import get_num_words, get_char_count, get_sorted_char_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    with open(book_path) as f:
        file_contents = f.read()
        word_count = get_num_words(file_contents)
        char_count = get_char_count(file_contents)
        sorted_chars = get_sorted_char_list(char_count)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(word_count)
        print("--------- Character Count -------")
        for char_dict in sorted_chars:
            if char_dict["char"].isalpha():
                print(f"{char_dict['char']}: {char_dict['num']}")
        print("============= END ===============")

main()
