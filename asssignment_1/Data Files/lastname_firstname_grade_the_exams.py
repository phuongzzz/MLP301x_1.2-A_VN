import pandas as pd
import numpy as np

ANSWER_KEY = np.array("B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".split(","))

# Task 1
def open_class_file():
    while True:
        name = input("Enter a class file to grade (i.e. class1 for class1.txt): ").strip()
        try:
            with open(name + ".txt", "r") as f:
                lines = f.read().splitlines()
            print(f"Successfully opened {name}.txt")
            return name, lines
        except FileNotFoundError:
            print("File cannot be found.")

# Task 2
def analyze(lines):
    print("**** ANALYZING ****")
    valid = []
    invalid_count = 0
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        values = line.split(",")
        if len(values) != 26:
            print("Invalid line of data: does not contain exactly 26 values:")
            print(line)
            invalid_count += 1
        elif not (values[0].startswith("N") and len(values[0]) == 9 and values[0][1:].isdigit()):
            print("Invalid line of data: N# is invalid")
            print(line)
            invalid_count += 1
        else:
            valid.append(values)
    if invalid_count == 0:
        print("No errors found!")
    return valid, invalid_count

# Task 3
def grade(valid):
    ids, scores = [], []
    for values in valid:
        answers = np.array(values[1:])
        correct = np.sum(answers == ANSWER_KEY)
        skipped = np.sum(answers == "")
        wrong = 25 - correct - skipped
        ids.append(values[0])
        scores.append(int(4 * correct - wrong))
    return pd.DataFrame({"id": ids, "score": scores})


def report(df, valid_count, invalid_count):
    print("**** REPORT ****")
    print(f"Total valid lines of data: {valid_count}")
    print(f"Total invalid lines of data: {invalid_count}")
    if valid_count == 0:
        return
    s = df["score"].to_numpy()
    print(f"Mean (average) score: {np.mean(s):.2f}")
    print(f"Highest score: {np.max(s)}")
    print(f"Lowest score: {np.min(s)}")
    print(f"Range of scores: {np.max(s) - np.min(s)}")
    print(f"Median score: {np.median(s):g}")

# Task 4
if __name__ == "__main__":
    name, lines = open_class_file()
    valid, invalid_count = analyze(lines)
    df = grade(valid)
    report(df, len(valid), invalid_count)
    df.to_csv(f"{name}_grades.txt", header=False, index=False)