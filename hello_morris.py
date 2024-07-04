#Define a function and name it alternate_word that takes in an input_string
def alternate_word(input_string):
    words = input_string.split() #split the input_string int words and save them in a list called words
    result = []
    for word in words:
        alternate_word = ""
    for i, in enumerate(words):
        if i % 2 == 0:
            alternate_word += i.upper()
        else:
            alternate_word += i.lower()
    result.append(alternate_word)
    return ' '.join(result)

input_string = "Morrisa Munesu is just a wee gero"
output_string = alternate_word(input_string)

print(output_string)

