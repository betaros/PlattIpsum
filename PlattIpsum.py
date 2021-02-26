import json
import random

class PlattIpsum:

    def __init__(self, word_count) -> None:
        self.word_count = word_count
        self.load_words()
        random.seed()
        
    def load_words(self) -> None:
        with open("wordlist.json", "r") as json_file:
            self.words = json.load(json_file)
    
    def create_text(self) -> str:
        output = ""
        
        while self.word_count > 0:
            sentence_length = random.randint(1, 7)
            output = output + " " + self.sentence_structure(sentence_length)
            self.word_count = self.word_count - sentence_length

        return output

    def sentence_structure(self, words_left) -> str:
        sentence = ""
        sentence_words = []

        if words_left <= 1:
            sentence = self.get_random_word("noun").title()
        if words_left == 2:
            sentence = self.get_random_word("article").title() + " " + self.get_random_word("noun").title()
        if words_left == 3:
            sentence_words.append(self.get_random_word("personal_pronoun").title())
            sentence_words.append(self.get_random_word("irregular_verb"))
            sentence_words.append(self.get_random_word("adjective"))
            sentence = " ".join(sentence_words)
        if words_left == 4:
            sentence_words.append(self.get_random_word("article").title())
            sentence_words.append(self.get_random_word("noun").title())
            sentence_words.append(self.get_random_word("irregular_verb"))
            sentence_words.append(self.get_random_word("adjective"))
            sentence = " ".join(sentence_words)
        if words_left == 5:
            sentence_words = []
            sentence_words.append(self.get_random_word("possesive_pronoun").title())
            sentence = " ".join(sentence_words)                
        if words_left == 6:
            pass
        if words_left >= 7:
            pass

        sentence = sentence + "."

        return sentence

    def get_random_word(self, word_type) -> str:
        return self.words[word_type][len(self.words[word_type])-1]

plattIpsum = PlattIpsum(30)
print(plattIpsum.create_text())