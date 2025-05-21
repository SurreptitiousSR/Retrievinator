import csv
import random
import time

filename = "questions.csv"

def welcomeMenu():
    print("Welcome to Retrievinator!")

def randomQuestions():
    with open(filename, newline ='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader) # Get column names
        data = list(reader) # Read rest of the data

    for i, column_name in enumerate(header):
        print(f"{i + 1}: {column_name}")

    while True:
        try:
            choice = int(input("Enter the number of the column to pick a random quesion from: "))
            if 1 <= choice <= len(header):
                break
            else:
                print("Invalid number. Try again")
        except ValueError:
            print("Please enter a valid number")

    selected_column_data = [row[choice - 1] for row in data if len(row) > choice - 1]
    random_cell = random.choice(selected_column_data)
    print(f" {random_cell}")


welcomeMenu()
randomQuestions()
    
