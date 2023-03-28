class Wordle:
    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5

    def __init__(self, secret: str):
        self.secret: str = secret
        self.attempts = []
        pass

    def attempt(self, word: str):
        self.attempts.append(word)

    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret

    @ property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)

    @ property              # with @property decortor it changes the functianlity of the function, don't  have to call like regular function wordle.can_attempt() becomes wordle.can_attempt
    def can_attempt(self):
        return self.remaining_attempts == 0 and not self.is_solved

        pass
