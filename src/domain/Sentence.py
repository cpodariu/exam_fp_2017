import random

from copy import deepcopy


class Sentence(object):
    def __init__(self, str):
        self.__unscrambled = deepcopy(str)
        self.__sentence = str.split(" ")
        self.__make_sentence_into_list()
        self.__scramble_words()
        self.__points = 0
        for i in self.__sentence:
            self.__points += len(i)

    @property
    def unscrambled(self):
        return self.__unscrambled

    @property
    def points(self):
        """Returns the amount of points for this sentence"""
        return self.__points

    @property
    def sentence(self):
        return self.__sentence

    @sentence.setter
    def sentence(self, value):
        self.__sentence = value

    @property
    def nr_of_words(self):
        return self.__nr_of_words

    def __make_sentence_into_list(self):
        """Transforms the sentence into a list"""
        l = []
        for i in self.__sentence:
            l.append(Sentence.__make_word_into_list(i))
        self.__sentence = l

    @staticmethod
    def __make_word_into_list(word):
        """Takes a str type and returns a list of the characters

        Arguments:
            word =str

        Returns:
            l - list
        """
        l = []
        while word != "":
            l.append(word[0])
            word = word[1:]
        return l

    def __scramble_words(self):
        """Scrambles all the letters in all the words"""
        letters = []
        for i in self.__sentence:
            for j in i[1:-1]:
                letters.append(j)
        random.shuffle(letters)
        for i in self.__sentence:
            j = 1
            while j < len(i) - 1:
                i[j] = letters[0]
                del letters[0]
                j += 1

    def __str__(self):
        line = ""
        for i in self.__sentence:
            for j in i:
                line += j
            line += " "
        return line.rstrip()
