import random
import time
import os

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = f"{left} {operator} {right}"
    answer = eval(expr)
    return expr, answer

def main():
    wrong = 0
    if os.getenv("NON_INTERACTIVE", "false").lower() == "true":
        print("Running in non-interactive mode.")
    else:
        input("Press enter to start!")

    print("----------------------")
    start_time = time.time()

    for i in range(TOTAL_PROBLEMS):
        expr, answer = generate_problem()
        while True:
            if os.getenv("NON_INTERACTIVE", "false").lower() == "true":
                guess = str(answer)  # Automatically guess the correct answer
                print(f"Problem #{i + 1}: {expr} = {guess}")
            else:
                guess = input(f"Problem #{i + 1}: {expr} = ")
            if guess == str(answer):
                break
            wrong += 1

    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    print("----------------------")
    print(f"Nice work! You finished in {total_time} seconds!")

if __name__ == "__main__":
    main()
