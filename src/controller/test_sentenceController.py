from unittest import TestCase

from copy import deepcopy

from src.controller.SentenceController import SentenceController
from src.repository.SentenceRepo import SentenceRepository


class TestSentenceController(TestCase):
    def setUp(self):
        self.__repo = SentenceRepository()
        self.__ctrl = SentenceController(self.__repo)

    def test_get_current_state(self):
        sentence, points = self.__ctrl.get_current_state()
        assert type(sentence) == str
        assert type(points) == int

    def test_swap_letters(self):
        str = deepcopy((self.__ctrl.sentence))
        self.__ctrl.swap_letters(0, 1, 0, 2)
        assert str != self.__ctrl.sentence
        try:
            self.__ctrl.swap_letters(0, 2, 0 , 2)
            assert False
        except ValueError:
            assert True