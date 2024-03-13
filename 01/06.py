class MinMaxWordFinder:
    def __init__(self):
        self.long_words = set()
        self.short_words = list()
        self.min_length = 1000
        self.max_length = 0

    def add_sentence(self, sentence):
        sentence = sorted(sentence.split(), key=len)
        if len(sentence[0]) < self.min_length:
            self.min_length = len(sentence[0])
        if len(sentence[-1]) > self.max_length:
            self.max_length = len(sentence[-1])
        for word in sentence:
            if len(word) == self.max_length:
                self.long_words.add(word)
            if len(word) == self.min_length:
                self.short_words.append(word)
        self.long_words = set(filter(lambda x: len(x) == self.max_length, self.long_words))
        self.short_words = list(filter(lambda x: len(x) == self.min_length, self.short_words))

    def shortest_words(self):
        return sorted(self.short_words)

    def longest_words(self):
        return sorted(self.long_words)
