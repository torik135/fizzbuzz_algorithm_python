class Fizzbuzz:
	def __init__(self, n):
		self.n = n

	def fizzbuzz(n):
		for i in range(1, n):
			if i % 3 == 0 and i % 5 == 0:
				print('{}-FizzBuzz'.format(i))
			elif i % 3 == 0:
				print('{}-Fizz'.format(i))
			elif i % 5 == 0:
				print('{}-Buzz'.format(i))
			else:
				print(i)

fb = Fizzbuzz.fizzbuzz(100)
print(fb)