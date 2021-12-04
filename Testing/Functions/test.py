def nums(amount = 1):
	num = 0
	while True:
		if num == amount:
			return None
		yield num
		num += 1

def infinity_numbers(start = 1, step = 1, end = 1):
	while start != end:
		yield start
		start += step

def Print(*args):
	for i in args:
		print(i)

#Print(*nums(5))

#Print(*infinity_numbers(1, 1, 3))

'''-----------------------------------------------------------------'''

def counter(func):
	count = 0
	def wrapper(*args, **kwargs):
		nonlocal count
		func(*args, **kwargs)
		count += 1
		print(f"The func was given {count} times")
	return wrapper

@counter
def say_word(word : str):
	print(word)

#say_word("Oo!!")

'''-----------------------------------------------------------------'''

def func():
	results = {}
	def wrapper(num):
		nonlocal results
		if num not in results:
			results[num] = func(num)
			print(f"Adding to dictionary")
		else:
			print(F"already have one")
		print(f"Cache {results}")
		print(results)
	return wrapper

'''-----------------------------------------------------------------'''

def e():
	n = 1

	while True:
		yield (1 + 1/n) ** n
		n += 1

iter_obj = iter("Hello!")

'''-----------------------------------------------------------------'''

USERS = ['admin', 'guest', 'director', 'root', 'superstar']

user_hello = '''If you wanna go on, type Y\n'''

#yesno = input(user_hello)

#auth = yesno == "Y"
auth = False

def is_auth(func):
	def wrapper():
		if auth:
			func()
		else:
			print("I don't know you")
	return wrapper

if auth:
    username = input("Введите ваш username:")

def has_access(func):
	def wrapper():
		if username in USERS:
			func()
		else:
			print("I can't find you")
	return wrapper

		

@is_auth
@has_access
def from_db():
    print("some data from database")

#from_db()

'''-----------------------------------------------------------------'''

# map + filter
some_list = [i - 10 for i in range(20)]
new_list = [i ** 2 for i in some_list if i > 0]
def pow2(x): return x**2
def positive(x): return x > 0

#print(list(map(pow2, filter(positive, some_list))) == new_list)

'''-----------------------------------------------------------------'''

a = ["asd", "bbd", "ddfa", "mcsa"]
#print(*list(map(len, a)))
#print(list(map(str.upper, a)))
#print(*list(map(lambda x: x.upper(), a)))

'''-----------------------------------------------------------------'''