
class PrimeIterator:
    """Class to generate prime numbers from 1 to a number n using iterator"""

    def __init__(self, n):
        self.start = 1
        self.n = n

    def is_prime(self, num):
        if num <= 1:
            return
        for i in range(2, num):
            if num % i == 0:
                return
        return True

    def __iter__(self):
        self.current_value = self.start
        return self

    def __next__(self):
        for num in range(self.current_value, self.n):
            if self.is_prime(num):
                self.current_value = num + 1
                return num
        raise StopIteration


prime = PrimeIterator(10)

j = iter(prime)

print(next(j))
print(next(j))
print(next(j))
print(next(j))
print(next(j))


# Using the concept of generators to redefine the PrimeIterator class above.


def prime_generator(n):
    """Function to generate prime numbers from 2 to a number n using generator"""
    stop = n

    # check if stop number is 1 or less
    if stop <= 1:
        return

    for number in range(2, stop):
        for num in range(2, number):
            if number % num == 0:
                break
        else:
            yield number


for char in prime_generator(10):
    print(char)

    
