def get_num_words(text):
    return len(text.split())


def count_characters(text):
    letter_counts = {}
    letter_lowercased = text.lower()
    for letter in letter_lowercased:
        if letter.isalpha():
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    return letter_counts

def sort_on(items):
    return items["num"]

def sort_dictionary(letter_counts):
    new_letter_dict = []
    for key, value in letter_counts.items():
        new_letter_dict.append({"char": key, "num": value})
    
    new_letter_dict.sort(key=sort_on, reverse=True)
    return new_letter_dict