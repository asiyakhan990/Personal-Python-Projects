import random

words = [
    {"german": "der", "english": "the (masculine)"},
    {"german": "die", "english": "the (feminine/plural)"},
    {"german": "das", "english": "the (neuter)"},
    {"german": "und", "english": "and"},
    {"german": "sein", "english": "to be"},
    {"german": "in", "english": "in"},
    {"german": "ein", "english": "a, an (masculine/neuter)"},
    {"german": "zu", "english": "to, too"},
    {"german": "haben", "english": "to have"},
    {"german": "ich", "english": "I"},
    {"german": "werden", "english": "to become, will"},
    {"german": "sie", "english": "she, they"},
    {"german": "nicht", "english": "not"},
    {"german": "von", "english": "from, of"},
    {"german": "mit", "english": "with"},
    {"german": "es", "english": "it"},
    {"german": "sich", "english": "oneself"},
    {"german": "auch", "english": "also"},
    {"german": "auf", "english": "on, upon"},
    {"german": "für", "english": "for"},

]

def quiz_user(words):
    """Quiz the user with words."""
    random.shuffle(words)  
    score = 0

    for word in words:
        print(f"What is the English translation of '{word['german']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{word['english']}'.\n")

    print(f"Quiz complete! Your score: {score}/{len(words)}")

def main():
    print("Welcome to the Language Learning Flashcards App!")
    input("Press Enter to start the quiz...")
    quiz_user(words)

if __name__ == "__main__":
    main()