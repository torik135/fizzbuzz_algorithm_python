data = [i for i in range(1, 101)]

fizzbuzz = ["{}-FizzBuzz".format(i) if i % 3 == 0 and i % 5 == 0 else ("{}-Fizz".format(i) if i % 3 == 0 else ("{}-Buzz".format(i) if i % 5 == 0 else i)) for i in data]

print("Fizzbuzz\n", fizzbuzz)