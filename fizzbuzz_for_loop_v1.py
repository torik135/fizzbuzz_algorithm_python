data = [if for i in range(1, 101)]

for i in data:
	if i % 3 == 0 and i % 5 == 0:
		print('{}-FizzBuzz'.format(i))
	elif i % 3 == 0:
		print('{}-Fizz'.format(i))
	elif i % 5 == 0:
		print('{}-Buzz'.format(i))
	else:
		print(i)