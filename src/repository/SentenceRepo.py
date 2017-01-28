import random

from copy import deepcopy

from src.domain.Sentence import Sentence


class SentenceRepository(object):
    def __init__(self):
        self.__sentences = self.read_from_file()
        self.__current_sentence = Sentence(random.choice(self.__sentences))
        self.__history = []

    def make_history(self):
        """Stores current sentence into the history"""
        self.__history.append(deepcopy(self.__current_sentence))

    def remember_history(self):
        """Gets the last sentence from the history"""
        self.__history.pop()
        self.__current_sentence = self.__history.pop()

    def read_from_file(self):
        """reads every line from the file and returns it into a list

        Returns:
            a - list
        """
        with open('sentences.txt', 'r') as f:
            a = (f.read()).split('\n')
            return a

    @property
    def unscrambled(self):
        return self.__current_sentence.unscrambled

    @property
    def sentence(self):
        return self.__current_sentence