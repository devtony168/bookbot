def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")                       # prints 1st line of report
    print(f"{get_num_words(text)} words found in the document")         # prints number of words of the text
    print("")  

    char_report = sort_on(text)                                         # generating char report
    for char in char_report:
        print(f"The '{char}' character was found {char_report[char]} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(book_text):
    return len(book_text.split())

def get_num_letter(book_text):
    num_letter = {}
    for letter in book_text: 
        lowered_letter = letter.lower()
        if lowered_letter not in num_letter:
            num_letter[lowered_letter] = 1
        else:
            num_letter[lowered_letter] += 1
    return num_letter

def second_element(tuple):
    return tuple[1]                                         # returns second element of tuple for sort function

def sort_on(book_text):
    alpha_dict = {}
    num_letter = get_num_letter(book_text)
    for letter in num_letter:                               # alpha letter filter for new dict
        if letter.isalpha():
            alpha_dict[letter] = num_letter[letter]

    alpha_tuple = list(alpha_dict.items())
    alpha_tuple.sort(reverse=True, key=second_element)      # descending by value, function as argument for the key parameter

    return dict(alpha_tuple)                                # returns tuple as dict


main()