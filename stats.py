def count_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_count = {}
    
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in char_count:
            char_count[lowercase_char] += 1
        else:
            char_count[lowercase_char] = 1
            
    return char_count

def sort_characters(char_counts):
    chars_list = []
    for char, count in char_counts.items():
        chars_list.append({"char": char, "num": count})
    
    chars_list.sort(reverse=True, key=lambda d: d["num"])
    
    return chars_list