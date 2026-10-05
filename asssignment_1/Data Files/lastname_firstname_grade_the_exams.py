import pandas as pd
import numpy as np

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

def report(valid_count, invalid_count):
    print("**** REPORT ****")
    print(f"Total valid lines of data: {valid_count}")
    print(f"Total invalid lines of data: {invalid_count}")

if __name__ == "__main__":
    name, lines = open_class_file()
    valid, invalid_count = analyze(lines)
    report(len(valid), invalid_count)