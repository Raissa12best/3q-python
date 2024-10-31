def word_frequencies(sentence):
    words = sentence.split()
    frequencies = {}

    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1

    return frequencies

sentence = "the quick brown fox jumps over the lazy dog"
print(word_frequencies(sentence))
