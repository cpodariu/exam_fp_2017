from unittest import TestCase

from src.repository.SentenceRepo import SentenceRepository


class TestSentenceRepository(TestCase):
    def setUp(self):
        self.__repo = SentenceRepository()

    def test_sentence(self):
        a = self.__repo
        assert (type(a) == SentenceRepository)
        assert (type(str(a)) == str)
