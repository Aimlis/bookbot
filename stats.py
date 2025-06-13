#turns file into lowercase string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        only_lower_case = file_contents.lower()
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}")
    return only_lower_case


#counts the words in a string
def count_words(text):
    words = text.split()
    num_words = len(words)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    return num_words

#creates a dict that counts all characters
def character_counter(text):
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

    
def print_sorted_report(char_dict):
    print("--------- Character Count -------")
    
    # Sort the items by value, descending
    sorted_items = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    
    # Print each character and its count
    for char, count in sorted_items:
        if char.isalpha() == True:
            print(f"{char}: {count}")
    
    print("============= END ===============")

