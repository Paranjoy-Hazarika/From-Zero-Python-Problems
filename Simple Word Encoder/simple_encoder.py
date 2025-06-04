encoder = "HELLO"
words = []

sentence = input("Enter your sentence: ")

for word in sentence.split(","):
    words.append(word.strip());

if encoder in words:
    print("Greetings recieved!")
else:
    print("Unauthorized message!")
