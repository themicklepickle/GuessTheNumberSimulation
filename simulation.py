import random
import time


def new_scope(old_scope, guess, target):
    if guess < target:
        updated_scope = (guess + 1, old_scope[1])
    elif guess > target:
        updated_scope = (old_scope[0], guess - 1)
    else:
        updated_scope = old_scope
    return updated_scope


def clear_data():
    data = open("data.csv", "w")
    data.write(f"level,winner,guesses\n")
    data.close()


def simulation():
    start_time = time.time()
    for i in range(1, 15):
        for j in range(2 ** i):
            data = open("data.csv", "a")

            level = random.randint(1, 4)

            p1_scope = (1, 10 ** level)
            p2_scope = p1_scope

            p1_target = random.randint(p1_scope[0], p1_scope[1])
            p2_target = random.randint(p2_scope[0], p2_scope[1])

            p1_guess = p1_target - 1
            p2_guess = p2_target - 1
            guesses = 0

            while p1_guess != p1_target and p2_guess != p2_target:
                guesses += 1

                p1_guess = int(random.randint(p1_scope[0], p1_scope[1]))
                p2_guess = int(random.randint(p2_scope[0], p2_scope[1]))

                p1_scope = new_scope(p1_scope, p1_guess, p1_target)
                p2_scope = new_scope(p2_scope, p2_guess, p2_target)

            if p1_guess == p1_target and p2_guess == p2_target:
                winner = "tie"
            elif p1_guess == p1_target:
                winner = "p1"
            elif p2_guess == p2_target:
                winner = "p2"

            data.write(f"{level},{winner},{str(guesses)}\n")

            data.close()
        end_time = time.time()
        print(f"{2 ** i}: {end_time - start_time}")


simulation()
