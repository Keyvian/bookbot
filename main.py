from stats import get_num_words, get_char_count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(get_num_words(file_contents))
        print(get_char_count(file_contents))

main()
