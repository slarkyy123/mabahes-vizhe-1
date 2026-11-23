#نیما مرتضائی
from collections import Counter


def analyze_string(text):

    # 1. Count words
    words = text.split()
    word_count = len(words)

    # 2. Count characters (excluding spaces)
    character_count = len(text.replace(" ", ""))

    # 3. Find the most frequent character
    characters = [char.lower() for char in text if not char.isspace()]
    char_frequency = Counter(characters)

    if char_frequency:
        most_frequent_char = char_frequency.most_common(1)[0]
    else:
        most_frequent_char = None

    # 4. Count the frequency of each word
    word_frequency = Counter(word.lower() for word in words)

    # Display results
    print("\n========== STRING ANALYSIS ==========")

    print(f"Number of words: {word_count}")

    print(f"Number of characters: {character_count}")

    if most_frequent_char:
        print(
            f"Most frequent character: "
            f"'{most_frequent_char[0]}' "
            f"({most_frequent_char[1]} times)"
        )
    else:
        print("No characters found.")

    print("\nWord frequency:")

    for word, count in word_frequency.items():
        print(f"{word}: {count} times")

    print("=====================================")


# Main program
user_text = input("Enter a text: ")

analyze_string(user_text)