def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    characters = {}
    for char in text.lower():
        if char.isalpha():
            characters[char] = characters.get(char, 0) + 1
    return characters

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def sort_on(items):
    return items["num"]

def dictionary_to_sorted_list(dictionary):
    new_list = []
    for key, value in dictionary.items():
        new_list.append({"char": key, "num": value})
    new_list.sort(reverse=True, key=sort_on)
    return new_list
 

def print_report(word_count, character_count, path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in character_count:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
