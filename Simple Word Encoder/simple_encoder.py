def check_secret_word(sentence, secret_word):
    if sentence == "":
        return "Empty sentence - Unauthorized message!"

    words = []

    for word in sentence.split(","):
        words.append(word.strip())

    if secret_word in words:
        return "Greetings recieved!"
    else:
        return "Unauthorized message!"


if __name__ == "__main__":
    secret_word = "HELLO"
    words = []

    sentence = input("Enter your sentence: ")
    result = check_secret_word(sentence, secret_word)
    print(result)
