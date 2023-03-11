from anagram_checker import AnagramChecker

def validate_input(word):
    if len(word.split()) > 1:
        print("Error: Only a single word is allowed.")
        return False
    if not word.isalpha():
        print("Error: Only alphabetic characters are allowed.")
        return False
    return True

def show_menu():
    print("\n\nWelcome to the Anagram Checker!")
    print("Choose an option:")
    print("1. Enter a word")
    print("2. Exit")

anagram_checker = AnagramChecker('sowpods.txt')

while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        word = input("Enter a word: ").strip()
        if validate_input(word):
            if anagram_checker.is_valid_word(word):
                anagrams = anagram_checker.get_anagrams(word)
                print(f"\n\nYOUR WORD: '{word.upper()}'")
                print("This is a valid English word.")
                if anagrams:
                    print("Anagrams for your word: " + ", ".join(anagrams))
                else:
                    print("No anagrams found for your word.")
            else:
                print(f"\n\n'{word.upper()}' is not a valid English word.")
    elif choice == '2':
        break
    else:
        print("Invalid choice. Please choose again.")
