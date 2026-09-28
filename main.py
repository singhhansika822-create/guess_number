# Guess the Number Game

A simple Python command-line game where the computer randomly selects a number between **1 and 100**, and the player tries to guess it.

## Features

- Generates a random number between 1 and 100.
- Accepts guesses from the user.
- Counts the number of valid attempts.
- Gives hints when the guess is too high or too low.
- Displays **"Very close!"** when the guess is within 5 of the target.
- Handles invalid non-numeric input.
- Rejects numbers outside the range 1–100.
- Handles `EOFError` and exits the game gracefully.

## Requirements

- Python 3.x
- No external libraries are required. The program uses Python's built-in `random` module.

## How to Run

1. Save the Python code in a file, for example:

   `guess_number.py`

2. Open a terminal or command prompt in the folder containing the file.

3. Run:

   ```bash
   python guess_number.py
   ```

## How to Play

1. The computer chooses a random number between 1 and 100.
2. Enter your guess when prompted.
3. The game provides a hint:
   - **Too low!** — your guess is smaller than the target.
   - **Too high!** — your guess is larger than the target.
   - **Very close!** — your guess is within 5 of the target.
4. Continue guessing until you find the correct number.
5. The game displays the number of attempts used.

## Example

```text
Welcome to the Guess the Number Game!
I'm thinking of a number between 1 and 100. Can you guess it?
Enter your guess: 40
Too low! Try a higher number.
Enter your guess: 70
Very close! Keep trying.
Enter your guess: 74
Congratulations! You guessed it in 3 attempts.
```

*Note: The target number is randomly generated, so the example output will vary each time.*

## Code Overview

### `play_game()`

The `play_game()` function contains the main game logic:

- Prints the welcome message.
- Generates the target number using `random.randint(1, 100)`.
- Repeatedly asks the player for a guess.
- Validates the input.
- Compares the guess with the target.
- Provides an appropriate hint.
- Ends the game when the correct number is guessed.

### Input Handling

The program uses `try-except` to handle invalid input:

```python
try:
    guess = int(input("Enter your guess: "))
except ValueError:
    print("Invalid input. Please enter a number between 1 and 100.")
```

If the user enters something that cannot be converted to an integer, the program asks for another guess instead of crashing.

## Technologies Used

- **Language:** Python
- **Module:** `random`
- **Interface:** Command Line / Terminal

## Author

Created by Hansika Singh.
