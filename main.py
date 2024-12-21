def charCounter(file_contents):
    lowered_string = file_contents.lower()
    charDictionary = {}
    for char in lowered_string:  # No need to use .split here
        if char.isalnum():  # Consider only alphanumeric characters
            charDictionary[char] = charDictionary.get(char, 0) + 1
    return charDictionary

def generateReport(word_count, char_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    # Convert the character dictionary to a sorted list of dictionaries
    sorted_chars = sorted(char_count.items(), key=lambda item: item[0])  # Sort alphabetically
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


if __name__ == '__main__':
    with open('/Users/blevin/workspace_personal/github.com/Benefit00/bookbot/books/frankenstein.txt', 'r') as f:
        file_contents = f.read()

        words = file_contents.split()
        word_count = len(words)

        char_count = charCounter(file_contents)

    print(f"Word count: {word_count}")
    print("Character count:")
    for char, count in sorted(char_count.items()):
        print(f"{char}: {count}")

    generateReport(word_count, char_count)