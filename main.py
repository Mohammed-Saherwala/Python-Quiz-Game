questions = ("What is the largest planet in our solar system?",
             "What is the chemical symbol for gold?",
             "Who painted the Mona Lisa?",
             "What is the capital city of Canada?",
             "What year did the first iPhone release?",
             "What is 12 * 7?",
             "Which animal is known as the king of the jungle?",
             "What gas do humans need to breathe to survive?",
             "What video game features the character Link?",
             "What is the fastest land animal in the world?")

options = (("A. Earth ","B. Jupiter ","C. Saturn ","D. Neptune "),
           ("A. Au ","B. Ag ","C. Go ","D. Gd "),
           ("A. Vincent Van Gogh ","B. Pablo Picasso ","C. Leonardo Da Vinci ","D. Claude Monet "),
           ("A. Toronto ","B. Vancouver ","C. Montreal  ","D. Ottava "),
           ("A. 2005 ","B. 2007 ","C. 2009 ","D. 2011 "),
           ("A. 72 ","B. 74 ","C. 96 ","D. 84 "),
           ("A. Tiger ","B. Lion ","C. Elephant ","D. Gorilla "),
           ("A. Carbon-Dioxide ","B. Nitrogen ","C. Oxygen ","D. Hydrogen "),
           ("A. Minecraft ","B. The Legend of Zelda ","C. Fortnite ","D. Roblox "),
           ("A. Cheetah ","B. Falcon ","C. Horse ","D. Leopard "))

answers = ("B","A","C","D","B","D","B","C","B","A")

guesses = []
score = 0
question_num = 0

print("Welcome to the game!")

for question in questions:
    print("--------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter your guess (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} was the correct answer!")
    question_num += 1

score = score / len(questions) * 100
print("------------------------------------------")
print(f"Your final score is: {score}%")

while True:
    if score == 100:
        print("You got them all right! Good job!")
        break
    elif score < 100:
        retry = input("Would you like to retry? (Y/N): ").upper()
        if retry == "N":
            print("Thank you for trying my game! See you later!")
            break
        else:
            score = 0
            question_num = 0
            guesses = []
            for question in questions:
                print("--------------------------------------------")
                print(question)
                for option in options[question_num]:
                    print(option)

                guess = input("Enter your guess (A, B, C, D): ").upper()
                guesses.append(guess)
                if guess == answers[question_num]:
                    score += 1
                    print("Correct!")
                else:
                    print("Incorrect!")
                    print(f"{answers[question_num]} was the correct answer!")
                question_num += 1

            score = score / len(questions) * 100
            print(f"Your final score is: {score}%")





