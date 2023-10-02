# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if self.seconds < 59:
            self.seconds += 1
        else:
            if self.minutes < 59:
                self.minutes += 1
                self.seconds = 0
            else:
                self.seconds = 0
                self.minutes = 0

    def __str__(self):
        return f"{self.minutes:02d}:{self.seconds:02d}"

# watch = Stopwatch()
# for i in range(3600):
#     print(watch)
#     watch.tick()
