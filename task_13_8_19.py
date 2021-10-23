def main():
    cnt = int(input('How many tickets do you wanna buy?\n'))
    youth = adult = 0

    try:
        ages = list(map(int, input("What are the ages of the visitors?\n").split()))
        #ages = [int(input()) for i in range (cnt)]
    except ValueError as e:
        print("It's a strange age...")

    for age in ages:
        if age > 25:
            adult += 1
        elif age >= 18:
            youth += 1

    result = float ((youth * 990 + adult * 1390) * (0.9 if cnt > 3 else 1))
    print(f"You have to pay O_o\n{result} ₽" if result else "You don't have to pay =)")

if __name__=="__main__":
    main()
