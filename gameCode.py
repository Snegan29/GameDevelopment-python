def main():
questions = [
    "1.Do you ever talk to yourself in the mirror?",
    "2.Can you fold a piece of paper in half more than 7 times?",
    "3.Have you ever tried to eat a clock?",
    "4.Will you see a figure if you stare at a corner of your room?",
    "5.Can you step on a shadow?",
    "6.Can you name a color that doesn't have the letter 'e' in it?",
    "7.Do you think dogs can read our minds?",
    "8.Is it possible to sneeze with your eyes open?",
    "9.Are you living in a Simulation?",
    "10.Choose between 'Yes' or 'No'?" 
]

answers = {
    "1.Do you ever talk to yourself in the mirror?": "YES",
    "2.Can you fold a piece of paper in half more than 7 times?": "NO",
    "3.Have you ever tried to eat a clock?": "NO",
    "4.Will you see a figure if you stare at a corner of your room?":"YES",
    "5.Can you step on a shadow?": "NO",
    "6.Can you name a color that doesn't have the letter 'e' in it?":"YES",
    "7.Do you think dogs can read our minds?": "NO",
    "8.Is it possible to sneeze with your eyes open?": "NO",
    "9.Are you living in a Simulation?": "YES",
    "10.Choose between 'Yes' or 'No'?": "OR" 
}

score = 0

for current_index in range(10):
    question = questions[current_index]
    print(question)
    answer = input("Enter 'YES' or 'NO': ".format(questions))

    if answer.upper() == answers[question]:
        score += 1
        print("Answer: Correct!")
    else:
        print("Answer: Incorrect. The answer is {}.".format(answers[question]))

print("You scored {} questions correctly out of 10.".format(score))
if __name__ == "__main__":
main()