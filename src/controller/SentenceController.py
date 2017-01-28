class SentenceController:
    def __init__(self, repo):
        self.__repo = repo
        self.__score = self.__repo.sentence.points

    def make_history(self):
        self.__repo.make_history()

    def remember_history(self):
        self.__repo.remember_history()

    @property
    def sentence(self):
        return self.__repo.sentence

    @property
    def unscrambled(self):
        return self.__repo.unscrambled

    def get_current_state(self):
        """returns information useful for printing current state

            Returns:
                self.__repo.__sentence - the current sentence
                self.__score - the current score
        """
        return str(self.__repo.sentence), self.__score

    def swap_letters(self, w1, l1, w2, l2):
        """Swaps the letters

        Arguments:
            w1 - int
            w2 - int
            l1 - int
            l2 - int

        Raises:
            IndexError if the words or letters don't exist
        """
        if w1 == w2 and l1 == l2:
            raise ValueError("You can't change a letter with itself")
        if l1 == 0 or l2 == 0:
            raise ValueError("You can't change the first letters")
        if l1 == len(self.__repo.sentence.sentence[w1]) - 1:
            raise ValueError("You can't change the last letters")
        if l2 == len(self.__repo.sentence.sentence[w2]) - 1:
            raise ValueError("You can't change the last letters")
        try:
            if w1 == w2 and l1 == l2:
                raise ValueError("You can't change a letter with itself")
            self.__repo.sentence.sentence[w1][l1], self.__repo.sentence.sentence[w2][l2] = \
                self.__repo.sentence.sentence[w2][l2], self.__repo.sentence.sentence[w1][l1]
            self.__score -= 1
        except IndexError:
            raise IndexError("List index out of range")
        except ValueError as f:
            raise ValueError(f)