
def create_files():

    large_words = []
    small_words = []

    with open('words.txt', 'r') as file:
        words = file.read().split()

    for word in words:
        if len(word) < 3:
            small_words.append(word)
        else:
            large_words.append(word)

    with open('small-words.txt', 'w') as small_file:
        for word in small_words:
            small_file.write(word + '\n')

    with open('large-words.txt', 'w') as large_file:
        for word in large_words:
            large_file.write(word + '\n')

    # Calculate total unique words
    unique_words = set(words)
    total_unique_words = len(unique_words)

    return total_unique_words


''
def ex3():
    total_words = create_files()
    print(f"Total words: {total_words}.")

ex3()