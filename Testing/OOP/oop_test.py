from accessify import protected, private, implements


class Test:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)


def main():
    a = Test("sasha")
    a.age = 53
    a.name = "not_sasha"
    a.get_name()
    print(a.age)


if __name__ == "__main__":
    main()
