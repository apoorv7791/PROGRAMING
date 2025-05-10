# check how many words that are occurring twice in a given sentence

sentence = input("Enter a sentence: ")
words = sentence.split()  # split the sentence into words
word_count = {}  # empty dictionary to store and count the words

for word in words:  # loop through the words
    if words.count(word) == 2:  # check if the word is occurring twice
        print(word)  # print the word
    else:
        continue

word_count[word] = words.count(word)  # add the word and its count to the dictionary
print("Word count: ", word_count)
