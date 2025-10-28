from stats import get_num_words, count_characters, sort_dictionary
import sys

def get_book_text(file_path):
    with open(file_path, "r") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")
    
    char_counts = count_characters(book_text)
    sorted_char_counts = sort_dictionary(char_counts)
    for char_count in sorted_char_counts:
        print(f"{char_count['char']}: {char_count['num']}")
    

if __name__ == "__main__":
    main()
