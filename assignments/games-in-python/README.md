
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a Hangman game using Python fundamentals such as strings, loops, conditionals, and user input. By completing this assignment, you will practice designing game logic and handling win/lose conditions.

## 📝 Tasks

### 🛠️ Build the Hangman Game Loop

#### Description
Create a Hangman game that randomly selects a word and repeatedly asks the player to guess one letter at a time.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list of words.
- Ask the player for letter guesses using input.
- Display the current word progress using underscores for unknown letters, for example: `_ _ _ _ _`.
- Keep a list or set of guessed letters and reveal all matching letters in the word.

### 🛠️ Handle Attempts and Game Outcomes

#### Description
Add rules for incorrect guesses, track remaining attempts, and end the game with clear outcome messages.

#### Requirements
Completed program should:

- Decrease remaining attempts only when a guessed letter is not in the word.
- Display the number of incorrect guesses remaining after each turn.
- End the game with a win message when the full word is guessed.
- End the game with a lose message when attempts reach zero, and show the correct word.
- Include sample run behavior similar to:
	```text
	Word: _ _ _ _
	Guess a letter: a
	Correct!
	Word: _ a _ _
	Attempts left: 5
	```
