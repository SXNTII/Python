# ================================================================
#                  THE PYTHON BOOK: GHOST CHASE
# ================================================================

# ======================== GAME SETTINGS ==========================

TOTAL_QUESTIONS = 15
STARTING_DISTANCE = 60
CORRECT_MOVE = 10
WRONG_MOVE = 20

score = 0
ghost_distance = STARTING_DISTANCE
game_over = False


# ======================== HELPER FUNCTIONS =======================

def heading(title):
    print("\n" + "=" * 64)
    print(f"{title:^64}")
    print("=" * 64)


def pause(message="Press ENTER to continue..."):
    input(f"\n{message}")


def get_input(message):
    return input(message).strip()


def show_ghost():
    print(r"""
                 .-======-.
               .'  o    o  '.
              /       ^      \
             |    .------.    |
             |    '------'    |
              \              /
               '._        _.'
                  /|    |\
                 /_|____|_\
    """)


def get_valid_answer():
    while True:
        answer = input("\nYour answer (A-D): ").strip().upper()

        if answer in ["A", "B", "C", "D"]:
            return answer

        print("Invalid choice! Please enter A, B, C, or D.")


# ======================== INTRODUCTION ===========================

def introduction():
    heading("THE PYTHON BOOK: GHOST CHASE")

    name = get_input("\nEnter your name: ")

    if not name:
        name = "Adventurer"

    print(f"\nWelcome, {name}!")
    print("\nYou are exploring an abandoned castle.")
    print("Inside, you discover an ancient book...")
    print("\n             THE PYTHON BOOK")
    print("\nIt contains mysterious lessons about Python programming.")

    pause("Press ENTER to open the book...")

    return name


# ======================== CHAPTERS ===============================

def read_chapter(title, lessons, next_message):
    heading(title)

    for lesson in lessons:
        print(f"• {lesson}")

    while True:
        action = input(f"\nType '{next_message}' to continue: ")
        action = action.strip().lower()

        if action == next_message:
            break

        print(f"Please type '{next_message}' to continue.")


def learning_section():
    read_chapter(
        "CHAPTER 1: PRELIM",
        [
            "Python was created by Guido van Rossum in 1991.",
            "Python uses indentation for code blocks.",
            "print() displays output on the screen.",
            "Variables store data and cannot start with a number."
        ],
        "next"
    )

    read_chapter(
        "CHAPTER 2: MIDTERM",
        [
            "input() gets information from the user.",
            "Math operators include +, -, *, and /.",
            "// is floor division and % is the remainder.",
            "Python follows PEMDAS in mathematical expressions."
        ],
        "next"
    )

    read_chapter(
        "CHAPTER 3: FINALS",
        [
            "Loops are used to repeat instructions.",
            "A for loop iterates over a sequence.",
            "A while loop repeats while a condition is True."
        ],
        "done"
    )


# ======================== QUESTIONS ==============================

questions = [
    # PRELIM
    {
        "period": "PRELIM",
        "q": "What is Python?",
        "choices": [
            "A. Programming language",
            "B. Computer",
            "C. Website",
            "D. Game"
        ],
        "answer": "A"
    },
    {
        "period": "PRELIM",
        "q": "Which function displays output?",
        "choices": [
            "A. input()",
            "B. print()",
            "C. len()",
            "D. int()"
        ],
        "answer": "B"
    },
    {
        "period": "PRELIM",
        "q": "Which symbol is used for comments?",
        "choices": [
            "A. //",
            "B. **",
            "C. #",
            "D. @"
        ],
        "answer": "C"
    },
    {
        "period": "PRELIM",
        "q": "Which data type stores whole numbers?",
        "choices": [
            "A. str",
            "B. int",
            "C. float",
            "D. bool"
        ],
        "answer": "B"
    },
    {
        "period": "PRELIM",
        "q": "Which function gets user input?",
        "choices": [
            "A. print()",
            "B. input()",
            "C. range()",
            "D. len()"
        ],
        "answer": "B"
    },

    # MIDTERM
    {
        "period": "MIDTERM",
        "q": "Which statement is used for decisions?",
        "choices": [
            "A. if",
            "B. print",
            "C. input",
            "D. import"
        ],
        "answer": "A"
    },
    {
        "period": "MIDTERM",
        "q": "Which keyword is used when the if condition is false?",
        "choices": [
            "A. for",
            "B. else",
            "C. while",
            "D. break"
        ],
        "answer": "B"
    },
    {
        "period": "MIDTERM",
        "q": "Which loop repeats a block of code?",
        "choices": [
            "A. print",
            "B. input",
            "C. for",
            "D. str"
        ],
        "answer": "C"
    },
    {
        "period": "MIDTERM",
        "q": "What does range(5) generate?",
        "choices": [
            "A. 1 to 5",
            "B. 0 to 4",
            "C. 0 to 5",
            "D. 1 to 4"
        ],
        "answer": "B"
    },
    {
        "period": "MIDTERM",
        "q": "Which operator checks equality?",
        "choices": [
            "A. =",
            "B. !=",
            "C. ==",
            "D. +="
        ],
        "answer": "C"
    },

    # FINALS
    {
        "period": "FINALS",
        "q": "What does len() return?",
        "choices": [
            "A. Number of items",
            "B. A random number",
            "C. A string",
            "D. A loop"
        ],
        "answer": "A"
    },
    {
        "period": "FINALS",
        "q": "Which keyword creates a function?",
        "choices": [
            "A. function",
            "B. def",
            "C. make",
            "D. create"
        ],
        "answer": "B"
    },
    {
        "period": "FINALS",
        "q": "Which collection uses square brackets?",
        "choices": [
            "A. Tuple",
            "B. Dictionary",
            "C. List",
            "D. Set"
        ],
        "answer": "C"
    },
    {
        "period": "FINALS",
        "q": "What does append() do?",
        "choices": [
            "A. Removes an item",
            "B. Adds an item",
            "C. Sorts a list",
            "D. Clears a list"
        ],
        "answer": "B"
    },
    {
        "period": "FINALS",
        "q": "Which keyword imports a module?",
        "choices": [
            "A. include",
            "B. using",
            "C. import",
            "D. add"
        ],
        "answer": "C"
    }
]


# ======================== GHOST CHASE ============================

def show_area(index):
    if index == 0:
        heading("PRELIM: THE CASTLE ENTRANCE")
        print("You enter the castle.")
        print("A strange shadow follows you.")

    elif index == 5:
        heading("MIDTERM: THE DARK HALLWAY")
        print("The hallway grows darker.")
        print("You hear footsteps getting closer...")

    elif index == 10:
        heading("FINALS: THE LAST CORRIDOR")
        print("The castle exit is finally visible!")
        print("But the ghost is right behind you!")


def show_question(index, item):
    print("\n" + "-" * 64)
    print(f"QUESTION {index + 1}/{TOTAL_QUESTIONS} [{item['period']}]")
    print("-" * 64)

    print(f"\nGhost Distance: {ghost_distance} meters")
    print(f"Score: {score}/{TOTAL_QUESTIONS}")
    print(f"\n{item['q']}")

    for choice in item["choices"]:
        print(choice)


def update_ghost(correct):
    global score, ghost_distance

    if correct:
        score += 1
        ghost_distance += CORRECT_MOVE
        print("\nCorrect! You move farther away from the ghost!")
    else:
        ghost_distance -= WRONG_MOVE
        print("\nWrong answer!")
        print("The ghost gets closer!")

    print(f"\nGhost Distance: {max(0, ghost_distance)} meters")

    if ghost_distance > 60:
        print("The ghost is falling behind!")
    elif ghost_distance > 30:
        print("The ghost is getting closer!")
    elif ghost_distance > 0:
        print("WARNING! THE GHOST IS RIGHT BEHIND YOU!")


def play_game():
    global game_over, ghost_distance

    heading("ESCAPE THE HAUNTED CASTLE")
    print("Answer all 15 Python questions to escape!")
    pause()

    for index, item in enumerate(questions):
        show_area(index)
        show_question(index, item)

        answer = get_valid_answer()
        correct = answer == item["answer"]

        update_ghost(correct)

        if not correct:
            print(f"Correct answer: {item['answer']}")

        if ghost_distance <= 0:
            game_over = True
            heading("THE GHOST CAUGHT YOU!")
            show_ghost()
            print("The ghost has caught up with you!")
            print("Your adventure ends inside the castle.")
            break

        pause("Press ENTER for the next question...")


# ======================== FINAL RESULTS ==========================

def show_results(name):
    heading("ESCAPE RESULTS")

    print(f"Player: {name}")
    print(f"Final Score: {score}/{TOTAL_QUESTIONS}")

    if not game_over:
        heading("ESCAPE SUCCESSFUL!")
        print("You answered all 15 questions!")
        print("You finally reach the castle entrance.")
        print("The ghost disappears into the darkness.")
        print("You escaped with THE PYTHON BOOK!")
    else:
        heading("GAME OVER")
        print("The ghost caught you inside the castle.")
        print("THE PYTHON BOOK remains behind.")

    print("\nThank you for playing THE PYTHON BOOK: GHOST CHASE!")


# ======================== MAIN PROGRAM ===========================

def main():
    player_name = introduction()
    learning_section()

    heading("SOMETHING IS FOLLOWING YOU")
    print("You finish reading the last chapter.")
    print("Suddenly, you hear footsteps behind you.")
    print("A mysterious ghost appears!")
    print("It wants the Python book you are holding.")
    print("Escape the castle before it catches you!")

    pause("Press ENTER to begin the escape...")

    play_game()
    show_results(player_name)


# RUN THE GAME
if __name__ == "__main__":
    main()
