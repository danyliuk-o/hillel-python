import string

text = input("Enter a string: ")

words = text.split()
print(words)
cleaned_words = []
for word in words:
    cleaned = "".join(char for char in word if char not in string.punctuation)
    if cleaned:
        cleaned_words.append(cleaned[0].upper() + cleaned[1:])

if cleaned_words:
    hashtag = "#" + "".join(cleaned_words)
    hashtag = hashtag[:140]
else:
    hashtag = ""

print(hashtag)
