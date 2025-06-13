from stats import get_book_text
from stats import character_counter
from stats import count_words
from stats import print_sorted_report

def main():
    wall_o_text = get_book_text("books/frankenstein.txt") #turns the book into a string
    ugly_dict = character_counter(wall_o_text) 
    num_words = count_words(wall_o_text)
    print_sorted_report(ugly_dict)
    


main()