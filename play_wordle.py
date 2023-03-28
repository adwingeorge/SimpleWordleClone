from wordle import Wordle


def main():

    print("hHello Wordle")
    wordle = Wordle('APPLE')

    while Wordle.can_attempt:
        x = input("Type your guess: ")
        wordle.attempt(x)

    if wordle.is_solved:
        print("you have solved the puzzle.")


if __name__ == "__main__":
    main()
