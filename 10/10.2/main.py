def first_word(text):
    i = 0
    while i < len(text) and not text[i].isalpha():
        i += 1
    start = i
    while i < len(text) and (text[i].isalpha() or text[i] == "'"):
        i += 1
    return text[start:i]

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
