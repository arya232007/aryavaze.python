import string

def print_words_of_length(filename, length):
    try:
        with open(filename, 'r') as file:
            text = file.read()

        # Remove punctuation
        translator = str.maketrans('', '', string.punctuation)
        text = text.translate(translator)

        words = text.split()

        # Filter words by specified length
        matching_words = [word for word in words if len(word) == length]

        print(f"\nWords of length {length}:")
        for word in matching_words:
            print(word)

    except FileNotFoundError:
        print("File not found. Please check the filename.")

# Example usage
filename = input("Enter the filename: ")
length = int(input("Enter the word length: "))
print_words_of_length(filename, length)
