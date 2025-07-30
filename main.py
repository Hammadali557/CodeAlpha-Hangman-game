import random

# Predefined list of words
word_list = ['apple', 'brain', 'snake', 'zebra', 'mouse']

# Select a random word
word_to_guess = random.choice(word_list)
guessed_letters = []
tries = 6

# ✅ Fixed this line
display_word = ['_'] * len(word_to_guess)

# Fake guessing letters one by one (simulate a player)
all_letters = list('abcdefghijklmnopqrstuvwxyz')
random.shuffle(all_letters)

print("🎮 Welcome to Hangman!")
print("Guess the word. You have 6 incorrect tries.\n")

for guess in all_letters:
    if tries == 0 or '_' not in display_word:
        break

    print("Word: ", ' '.join(display_word))
    print("Guessed letters: ", ', '.join(guessed_letters))
    print(f"Enter a letter: {guess}")

    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Correct!\n")
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                display_word[i] = guess
    else:
        print("❌ Incorrect guess.")
        tries -= 1
        print(f"Tries left: {tries}\n")

# Final result
if '_' not in display_word:
    print("🎉 Congratulations! You guessed the word:", word_to_guess)
else:
    print("💀 Game over! The word was:", word_to_guess)
