cnt = int(input('How many tickets do you wanna buy?\n'))
youth = 0
adult = 0
for i in range (cnt):
    age = int(input())
    if age < 0:
        print("You're not born yeat ;)")
    elif age < 18:
        continue
    elif 18 < age < 25:
        youth += 1
    else:
        adult += 1

result = float (youth * 990 + adult * 1390)
discount = 1 if cnt < 3 else 0.9
result *= discount
print(result)
