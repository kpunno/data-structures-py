
# rock, scissors, paper
def wins_rock_scissors_paper(p1, p2):
    result = False

    p1 = p1.upper()
    p2 = p2.upper()

    if ((p1 == "ROCK" and p2 == "SCISSORS") 
    or (p1 == "SCISSORS" and p2 == "PAPER") 
    or (p1 == "PAPER" and p2 == "ROCK")):
        result = True
        
    return result

# factorial
def factorial(n):
    n = int(n)
    result = n
    if (n <= 0):
        print("<n> must be a positive integer.")
    else:
        i = 2
        while i < n:
            result *= i
            i += 1
    return result

# fibonacci
def fibonacci(n):
    n = int(n)
    current = 1
    last = 0
    result = 0
    if (n <= 0):
        print("<n> must be a positive integer.")
    for i in range(n - 1):
        result = current + last
        last = current
        current = result
    return result

# sum_to_goal
def sum_to_goal(list, goal):
    goal = int(goal)
    for i in range(len(list)):
        for j in range(len(list)):
            if goal == (list[i] * list[j]):
                return list[i] * list[j]
    return 0

# up and down counter
class UpCounter:
    counter = 0
    stepSize = 1

    def __init__(self, stepSize):
        self.stepSize = stepSize

    def count(self):
        return self.counter

    def update(self):
        self.counter += self.stepSize

class DownCounter(UpCounter):
    def update(self):
        self.counter -= self.stepSize





