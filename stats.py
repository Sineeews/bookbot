def get_num_of_words(text):
    words = text.split()
    words_count = len(words)
    return words_count

def get_num_of_characters(text):
    characters = {}
    l_text = text.lower()
    for character in l_text:
        if character.isalpha():
            if character in characters:
                characters[character] += 1
            else:
                characters[character] = 1 
    return characters

def sort_on(char):
    return char["num"]

def get_sorted_characters(characters):
    sorted_characters = []
    for character in characters:
        temp_dict = {"char": character, "num": characters[character]}
        sorted_characters.append(temp_dict)
    sorted_characters.sort(reverse=True, key=sort_on)

    return sorted_characters