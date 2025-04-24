import sys
from stats import count_words, character_count, sort_characters

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def main():

    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    content = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path} ...")
    
    word_count = count_words(content)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    char_counts = character_count(content)
    sorted_chars = sort_characters(char_counts)

    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")

    print ("============= END ===============")


main()
