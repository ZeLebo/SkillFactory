from Tasks.OOP.Cat import Cat


def main():
    baron = Cat("Baron", "Boy", 2)
    sam = Cat("Sam", "Boy", 2)

    print(f"The name is {baron.name}, sex is {baron.sex} {baron.age} years old")
    print(f"The name is {sam.name}, sex is {sam.sex} {sam.age} years old")


if __name__ == '__main__':
    main()
