def main():
    adult = youth = 0
    try:
        cnt = int(input('How many tickets do you wanna buy?\n'))
        ages = list(map(int, input("What are the ages of the visitors?\n").split()))

    except ValueError as e:
        print("Your data is wrong, u don't trust me?")
        exit()

    for age in ages:
        if age > 25:
            adult += 1
        elif age >= 18:
            youth += 1

    result = float ((youth * 990 + adult * 1390) * (0.9 if cnt > 3 else 1))
    print(f"\nYou have to pay O_o\n{result} ₽" if result else "You don't have to pay =)")

if __name__=="__main__":
    main()
