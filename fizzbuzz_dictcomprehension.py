data = [i for i in range(1, 101)]

fizzbuzz = {k: "FizzBuzz".format(v) if v % 3 == 0 and v % 5 == 0 else ("Fizz".format(v) if v % 3 == 0 else ("Buzz".format(v) if v % 5 == 0 else v)) for k, v in zip(data, data)}

print("Fizzbuzz\n", fizzbuzz)