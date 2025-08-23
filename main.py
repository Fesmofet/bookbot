from stats import get_word_count, get_character_count, get_book_text, dictionary_to_sorted_list, print_report
import sys


def main():

    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = args[1]
    book_text = get_book_text(path_to_book)
    word_count = get_word_count(book_text)
    char_dict = get_character_count(book_text)
    sorted_char_list = dictionary_to_sorted_list(char_dict)
    print_report(word_count, sorted_char_list, path_to_book)

main()