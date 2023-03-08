# part 2
# i think need to rewrite tge part with bonus 
import string
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords


class Text:
    def __init__(self, text):
        self.text = text

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as file:
            text = file.read()
        return cls(text)

    def word_frequency(self, word):
        words = self.text.split()
        count = words.count(word)
        if count == 0:
            return None

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


class TextModification(Text):
    def __init__(self, text):
        super().__init__(text)

    def remove_punctuation(self):
        no_punct = self.text.translate(str.maketrans('', '', string.punctuation))
        return no_punct

    def remove_stopwords(self):
        words = self.text.split()
        no_stopwords = [word for word in words if word.lower() not in stopwords.words('english')]
        return ' '.join(no_stopwords)

    def remove_special_chars(self):
        no_special = self.text.encode('ascii', 'ignore').decode()
        return no_special


text = Text.from_file('the_stranger.txt')
print(text.word_frequency('the'))
print(text.most_common_word())
print(len(text.unique_words()))

text = TextModification.from_file('the_stranger.txt')
no_punct = text.remove_punctuation()
no_stopwords = text.remove_stopwords()
no_special = text.remove_special_chars()
print(no_punct[:100])
print(no_special[:100])
