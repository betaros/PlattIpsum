import json
import random


class PlattIpsum:

    def __init__(self) -> None:
        with open("wordlist.json", "r", encoding='utf-8') as json_file:
            self.words = json.load(json_file)

        random.seed()

    def create_text(self, word_count) -> str:
        self.word_count = word_count

        output = ""
        
        while self.word_count > 0:
            sentence_length = random.randint(1, 7)
            output = output + " " + self.sentence_structure(sentence_length)
            self.word_count = self.word_count - sentence_length

        return output

    def sentence_structure(self, words_left) -> str:
        sentence_words = []

        if words_left <= 1:
            sentence_words.append(self.get_random_word("noun").title())
        if words_left == 2:
            sentence_words.append(self.get_random_word("article").title())
            sentence_words.append(self.get_random_word("noun").title())
        if words_left == 3:
            sentence_words.append(self.get_random_word("personal_pronoun").title())
            sentence_words.append(self.get_random_word("irregular_verb"))
            sentence_words.append(self.get_random_word("adjective"))
        if words_left == 4:
            sentence_words.append(self.get_random_word("article").title())
            sentence_words.append(self.get_random_word("noun").title())
            sentence_words.append(self.get_random_word("irregular_verb"))
            sentence_words.append(self.get_random_word("adjective"))
        if words_left == 5:
            sentence_words.append(self.get_random_word("article").title())
            sentence_words.append(self.get_random_word("noun").title())
            sentence_words.append(self.get_random_word("irregular_verb"))
            sentence_words.append(self.get_random_word("pronoun"))
            sentence_words.append(self.get_random_word("adjective"))
        if words_left == 6:
            sentence_words.append(self.get_random_word("interogativ_question_pronoun").title())
            sentence_words.append(self.get_random_word("noun").title())
            sentence_words.append(self.get_random_word("irregular_verb"))
            sentence_words.append(self.get_random_word("article"))
            sentence_words.append(self.get_random_word("adjective"))
            sentence_words.append(self.get_random_word("noun").title())
        if words_left >= 7:
            sentence_words.append(self.get_random_word("personal_pronoun").title())
            sentence_words.append(self.get_random_word("verb"))
            sentence_words.append(self.get_random_word("numbers_unclear"))
            sentence_words.append(self.get_random_word("noun").title())
            sentence_words.append(self.get_random_word("article"))
            sentence_words.append(self.get_random_word("possesive_pronoun"))
            sentence_words.append(self.get_random_word("irregular_verb"))

        return " ".join(sentence_words) + "."

    def get_random_word(self, word_type) -> str:
        return self.words[word_type][random.randint(1, len(self.words[word_type])-1)]
