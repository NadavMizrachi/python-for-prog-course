from functools import reduce

text = "wellcome to Israel and have a good time!"

words = text.split()

longest_word = \
    reduce(
        lambda word1, word2:
            word1 if len(word1) > len(word2) else word2,
        words
    )

print(longest_word)
