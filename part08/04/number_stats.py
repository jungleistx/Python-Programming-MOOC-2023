# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.added = 0

    def add_number(self, number:int):
        self.added += 1
        self.numbers += number

    def count_numbers(self) -> int:
        return self.added

    def get_sum(self) -> int:
        return self.numbers

    def average(self) -> float:
        if self.added > 0:
            return self.numbers / self.added
        else:
            return 0

stats = NumberStats()
even_numbers = NumberStats()
odd_numbers = NumberStats()
print('Please type in integer numbers:')
while True:
    number = int(input())
    if number == -1:
        break
    stats.add_number(number)
    if number % 2 == 0:
        even_numbers.add_number(number)
    else:
        odd_numbers.add_number(number)

print(f'Sum of numbers: {stats.get_sum()}')
print(f'Mean of numbers: {stats.average()}')
print(f'Sum of even numbers: {even_numbers.get_sum()}')
print(f'Sum of odd numbers: {odd_numbers.get_sum()}')