from stats import get_book_text
from stats import character_counter
from stats import count_words
from stats import print_sorted_report
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
        wall_o_text = get_book_text(book) #turns the book into a string
        ugly_dict = character_counter(wall_o_text) 
        num_words = count_words(wall_o_text)
        print_sorted_report(ugly_dict)
    


main()