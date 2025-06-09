import string

def filter_word(sentence: str, bad_words: set) -> str:
    filtered_words = []
    for words in sentence.split():
        clean_word = words.strip(string.punctuation)

        if clean_word.lower() in bad_words:
            filtered_words.append("*" * len(clean_word))
        else:
            filtered_words.append(clean_word)

    
    return " ".join(filtered_words)


def main():
    bad_words = {"fuck", "bastard"}

    print("BAD WORD FILTER")
    
    while True:
        try:
            print("-" * 50)
            print("1. Filter Words")
            print("2. Exit")
            print("-" * 50)

            user_choice = int(input("Enter your choice: "))

            match user_choice:
                case 1:
                    while True:
                        print()
                        sentence = input("Enter your sentence: ")
                        
                        if not sentence.strip():
                            print("Please enter some text")
                            continue

                        cleaned_words = filter_word(sentence, bad_words)
                        print()
                        print("Filtered text:")
                        print("-" * 50)
                        print(f"{cleaned_words}")
                        break
                case 2:
                    print("Quiting...")
                    break
                case _:
                    print("Please enter a valid option (1 or 2)")
                    continue

        
        except ValueError:
            print("Please enter a number")
        except KeyboardInterrupt:
            print("\nTerminated by user")
            break


if __name__ == "__main__":
    main()