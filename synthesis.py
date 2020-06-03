import csv

NUM_LEVELS = 4

data = csv.reader(open("data.csv", "r"))
winners = [col[1] for col in data if col[1] != "winner"]
data = csv.reader(open("data.csv", "r"))
levels = [col[0] for col in data if col[0] != "level"]
data = csv.reader(open("data.csv", "r"))
guesses = [col[2] for col in data if col[2] != "guesses"]

# number of times each level was chosen
for i in range(NUM_LEVELS):
    print(f"level {i + 1}: {levels.count(f'{i + 1}')}")
print()

# number of times each player won
print(f"p1: {winners.count('p1')}")
print(f"p2: {winners.count('p2')}")
print(f"tie: {winners.count('tie')}\n")

# average guesses for each level
levels_guesses = zip(levels, guesses)
averages = [0] * NUM_LEVELS
for tup in levels_guesses:
    averages[int(tup[0]) - 1] += int(tup[1])
for i in range(len(averages)):
    averages[i] /= levels.count(str(i + 1))

print(averages)
