
import random

print("=" * 65)
print("          THE PYTHON BOOK: ABANDONED BUILDING ESCAPE")
print("=" * 65)

# Player name
name = input("\nEnter your name: ") or "Adventurer"

print("\nYou are exploring an abandoned 17-story building.")
print("You find THE PYTHON BOOK containing foundational Python lessons.")
input("\nPress ENTER to open the book...")

# Chapters
chapters = {
    "PRELIM": [
        "Python was created by Guido van Rossum in 1991.",
        "Python uses indentation. print() displays output."
    ],
    "MIDTERM": [
        "input() takes user data.",
        "Operators include +, -, /, //, and %."
    ],
    "FINALS": [
        "Loops repeat code. for iterates over sequences,",
        "while repeats as long as a condition is true."
    ]
}

for chapter, lessons in chapters.items():
    print("\n" + "=" * 65)
    print(f"                    CHAPTER: {chapter}")
    print("=" * 65)

    for lesson in lessons:
        print("- " + lesson)

    command = "done" if chapter == "FINALS" else "next"

    while input(f"\nType '{command}': ").lower() != command:
        pass

# Questions
questions = [
    ("PRELIM", "What is Python?",
     ["A. Programming language", "B. Computer", "C. Website", "D. Game"], "A"),

    ("PRELIM", "Which function displays output?",
     ["A. input()", "B. print()", "C. len()", "D. int()"], "B"),

    ("PRELIM", "Which symbol is used for single-line comments?",
     ["A. //", "B. --", "C. #", "D. @"], "C"),

    ("PRELIM", "Which data type represents whole numbers?",
     ["A. str", "B. int", "C. float", "D. bool"], "B"),

    ("PRELIM", "Which function captures user input?",
     ["A. print()", "B. input()", "C. range()", "D. len()"], "B"),

    ("MIDTERM", "Which keyword is used for conditional decisions?",
     ["A. if", "B. print", "C. input", "D. import"], "A"),

    ("MIDTERM", "Which keyword handles alternative outcomes?",
     ["A. for", "B. else", "C. while", "D. break"], "B"),

    ("MIDTERM", "Which loop iterates over sequences?",
     ["A. print", "B. input", "C. for", "D. str"], "C"),

    ("MIDTERM", "What numbers does range(5) generate?",
     ["A. 1 to 5", "B. 0 to 4", "C. 0 to 5", "D. 1 to 4"], "B"),

    ("MIDTERM", "Which operator checks value equality?",
     ["A. =", "B. !=", "C. ==", "D. +="], "C"),

    ("FINALS", "What does len() return?",
     ["A. Number of items", "B. Random number", "C. String", "D. Loop"], "A"),

    ("FINALS", "Which keyword stops a loop?",
     ["A. stop", "B. break", "C. end", "D. exit"], "B"),

    ("FINALS", "Which collection uses square brackets []?",
     ["A. Tuple", "B. Dictionary", "C. List", "D. Set"], "C"),

    ("FINALS", "What does append() do?",
     ["A. Removes an item", "B. Adds an item", "C. Sorts a list", "D. Clears a list"], "B"),

    ("FINALS", "Which keyword loads external modules?",
     ["A. include", "B. using", "C. import", "D. add"], "C")
]

random.shuffle(questions)

boss_question = (
    "FINAL BOSS: What is Sir Jomar's username in MU Online?",
    "JOMS927"
)

# Game variables
player_floor = 3
multo_floor = 1
exit_floor = 17
score = 0
cleared_floors = [player_floor]
escaped = False
game_over = False


def ask_question(question, choices=None):
    print("\n" + question)

    if choices:
        for choice in choices:
            print(choice)

    return input("\nAnswer: ").strip().upper()


def show_results():
    print("\n" + "=" * 65)
    print("                         FINAL RESULTS")
    print("=" * 65)
    print(f"Player: {name}")
    print(f"Final Score: {score}")

    if escaped:
        print("RESULT: SUCCESS!")
        print("You escaped through the rooftop!")
    else:
        print("RESULT: DEFEAT!")
        print("You were trapped inside the abandoned building.")

    print("=" * 65)
    print("                       END OF THE GAME")


print("\n" + "=" * 65)
print("                  THE PURSUIT BEGINS")
print("=" * 65)
print("A ghost (multo) appears on Floor 1!")
print("Start: Floor 3 | Goal: Roof Exit (Floor 17)")
print("Correct answer: Ghost climbs 1 floor.")
print("Wrong answer: Ghost climbs 2 floors.")
print("WARNING: The ghost gets closer after every move!")

input("\nPress ENTER to start...")

# Main game loop
while not game_over and not escaped:

    print("\n" + "=" * 65)
    print(f"       PLAYER: FLOOR {player_floor} | GHOST: FLOOR {multo_floor}")
    print(f"                       SCORE: {score}")
    print("=" * 65)

    distance = player_floor - multo_floor

    if distance <= 2:
        print("WARNING! The ghost is dangerously close!")

    possible_moves = [
        floor for floor in
        [player_floor - 1, player_floor + 1, player_floor + 2]
        if 2 <= floor <= exit_floor
    ]

    print(f"\nAvailable floors: {possible_moves}")

    while True:
        choice = input("Choose floor number: ")

        if choice.isdigit() and int(choice) in possible_moves:
            target_floor = int(choice)
            break

        print("Invalid floor! Choose from the available floors.")

    if target_floor in cleared_floors:
        player_floor = target_floor
        print(f"\nFloor {player_floor} is already cleared.")
        print("You move through the floor safely.")
        multo_climb = 1

    else:
        if target_floor == exit_floor:
            question, answer = boss_question
            period = "ROOF EXIT"
            choices = None

            print("\nYou have reached the rooftop!")
            print("A final boss is guarding the exit...")
            print("Answer correctly to escape!")

        else:
            period, question, choices, answer = questions.pop()

        print(f"\n--- FLOOR {target_floor} LOCKED [{period}] ---")

        user_answer = ask_question(question, choices)

        if user_answer == answer:
            score += 1
            player_floor = target_floor
            cleared_floors.append(player_floor)
            multo_climb = 1

            print("\nCORRECT! Door unlocked.")

            if player_floor == exit_floor:
                escaped = True

                print("\n" + "=" * 65)
                print("                     ROOF EXIT UNLOCKED!")
                print("=" * 65)
                print(f"{name}, you escaped the abandoned building!")
                print("You defeated the final boss!")
                print("The ghost could not catch you.")
                print("You survived the 17-story nightmare!")
                break

        else:
            print(f"\nINCORRECT! Correct answer: {answer}")
            print("The door is jammed!")
            print("You cannot move to the next floor.")
            multo_climb = 2

    # Ghost movement
    multo_floor += multo_climb

    print(f"\nThe ghost climbs {multo_climb} floor(s).")
    print(f"The ghost is now on Floor {multo_floor}!")

    # Game-over check
    if player_floor <= multo_floor:
        game_over = True

        print("\n" + "=" * 65)
        print("                       GHOST CAUGHT YOU!")
        print("=" * 65)

        print(r"""
                  .-''''''''''-.
                .'   _      _   '.
               /    (o)    (o)    \
              |                 |
              |       BOO!      |
              |     \______/    |
               \               /
                '.           .'
                  '-.____.-'
                     |  |
                    /    \
                   /      \
        """)

        print("The ghost caught you inside the abandoned building.")
        print("GAME OVER.")

    elif player_floor - multo_floor <= 2:
        print("\nWARNING! The ghost is getting dangerously close!")

# Final results
show_results()
