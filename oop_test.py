class test:
    def __init__(self, name):
        self.name = name


    def get_name(self):
        print(self.name)


def main():
    a = test("sasha")
    a.get_name()


if __name__=="__main__":
    main()
