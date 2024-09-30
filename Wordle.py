########################################
# Name:Gulfam Khan
# Collaborators (if any):N/A
# GenAI Transcript (if any):
# Estimated time spent (hr):6
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    gw = WordleGWindow()

    # Choose a random 5-letter word from the English words list
    secret_word = random.choice([word for word in ENGLISH_WORDS if len(word) == 5]).lower()
    gw.show_message("Guess the word!")

    def enter_action():
        current_row = gw.get_current_row()
        guess = word_from_row(current_row).lower()

        # Check if the guess is valid
        if len(guess) == 5 and is_english_word(guess):
            color_row(current_row, guess, secret_word)
            gw.set_current_row(current_row + 1)  # Move to the next row

            # Check if the guess is correct
            if guess == secret_word:
                gw.show_message("Congratulations! You've guessed the word!")
                gw.set_current_row(N_ROWS)  # End the game
        else:
            gw.show_message("Not in word list or not a 5-letter word.")

        # Reveal the answer if we've reached the last row
        if current_row + 1 == N_ROWS:
            gw.show_message("The secret word was: " + secret_word)

    gw.add_enter_listener(enter_action)

    def word_from_row(row: int) -> str:
        # Build the guessed word from the current row
        return ''.join(gw.get_square_letter(row, i) for i in range(N_COLS))

    def color_row(row: int, guess: str, secret: str):
        secret_used = [False] * 5  # Track which letters in the secret have been matched
        guess_used = [False] * 5    # Track which letters in the guess have been matched

        # First, mark correct letters (green)
        for i in range(5):
            if guess[i] == secret[i]:
                gw.set_square_color(row, i, CORRECT_COLOR)
                secret_used[i] = True
                guess_used[i] = True

        # Then, mark present letters (yellow)
        for i in range(5):
            if not guess_used[i] and guess[i] in secret:
                for j in range(5):
                    if guess[i] == secret[j] and not secret_used[j]:
                        gw.set_square_color(row, i, PRESENT_COLOR)
                        secret_used[j] = True  # Mark this letter as used
                        break

        # Finally, mark missing letters (gray)
        for i in range(5):
            if not guess_used[i]:
                gw.set_square_color(row, i, MISSING_COLOR)

# Start the game
if __name__ == "__main__":
    wordle()
