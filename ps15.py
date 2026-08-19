def count_words(sentence):
    words = sentence.lower().split()
    word_counts = {}
    for word in words:
        word = word.strip(".,!?:;")
        if word:
            word_counts[word] = word_counts.get(word, 0) + 1
            
    return word_counts
text = "Cat sat on a mat and the cat sat."
print(count_words(text))
