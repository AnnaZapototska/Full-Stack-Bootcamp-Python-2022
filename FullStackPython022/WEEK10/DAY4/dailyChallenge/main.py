# Part 1
class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.split()
        count = words.count(word)
        if count == 0:
            return None
        else:
            return f'The word "{word}" appears {count} times in the text.'

    def most_common_word(self):
        words = self.text.split()
        word_count = {}
        for word in words:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
        if len(word_count) == 0:
            return None
        else:
            return max(word_count, key=word_count.get)

    def unique_words(self):
        words = self.text.split()
        unique = list(set(words))
        return unique


text = Text("A good book would sometimes cost as much as a good house.")
print(text.word_frequency("good"))
print(text.most_common_word())
print(text.unique_words())


