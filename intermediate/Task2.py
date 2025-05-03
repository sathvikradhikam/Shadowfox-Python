import random

# Word list with hints
words_with_hints = [
    ("python", "A popular programming language"),
    ("elephant", "The largest land animal"),
    ("guitar", "A musical instrument with strings"),
    ("planet", "Orbits a star"),
    ("pizza", "A popular Italian dish"),
]

# Randomly select a word and its hint
word, hint = random.choice(words_with_hints)
guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("🎉 Welcome to Hangman!")
print(f"Hint: {hint}")

# Main game loop
while attempts > 0 and "_" in guessed:
    print("\nCurrent word:", " ".join(guessed))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Attempts left: {attempts}")
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Good guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        print("❌ Wrong guess!")
        attempts -= 1

# Result
if "_" not in guessed:
    print(f"\n🎉 Congratulations! You guessed the word: {word}")
else:
    print(f"\n💀 Game Over! The word was: {word}")
