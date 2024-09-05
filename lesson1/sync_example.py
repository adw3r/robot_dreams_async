import time


def say(what, when):
    time.sleep(when)
    print(what)


def main():
    say("Martin", 2)
    say("Bob", 1)
    say("Alice", 3)


if __name__ == "__main__":
    main()
