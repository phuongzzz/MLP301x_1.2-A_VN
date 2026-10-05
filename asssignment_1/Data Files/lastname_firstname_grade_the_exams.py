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


if __name__ == "__main__":
    name, lines = open_class_file()