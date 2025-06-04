# Simple Word Encoder

A simple Python program that checks if a specific encoded word is present in a user's input message.

## Description

This program takes a user's input sentence and checks if it contains the encoded word "HELLO". The program splits the input by commas and verifies if the encoded word exists in the message.

## Features

- Takes user input for message verification
- Splits messages by comma delimiter
- Checks for the presence of the encoded word "HELLO"
- Provides feedback based on message verification

## How to Use

1. Run the program
2. Enter your message when prompted
3. Separate words with commas if you want to check multiple words
4. The program will respond with:
   - "Greetings received!" if the encoded word is found
   - "Unauthorized message!" if the encoded word is not found

## Example

```
Enter your sentence: HELLO, World!
Greetings received!

Enter your sentence: Hi, there!
Unauthorized message!
```

## How to Run

```bash
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
```