def sort_on(items):
    return items["num"]

def get_word_count(text):
    word_list = text.split()
    return len(word_list)

def get_char_count(text):
    char_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_dict(dict):
    char_list = []
    for char in dict:
        num = dict[char]
        char_list.append({"char": char, "num": num})
    char_list.sort(reverse= True, key=sort_on)
    return char_list
