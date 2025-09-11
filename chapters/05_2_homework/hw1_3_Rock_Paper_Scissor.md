# Chapter 5 - Rock Paper Scissors

## Exercise – Rock, Paper, Scissors

In this exercise, you are going to practice using conditionals (`if`, `elif`, `else`). You will write a small program that will determine the result of a rock, paper, scissors game, given Player 1 and Player 2’s choices. Your program will print out the result. Here are the rules of the game:

1. **Create a Truth Table**: First create a truth table for all the possible choices for Player 1 and Player 2, and the outcome of the game. This will help you figure out how to code the game!

   | Player 1 | Player 2 | Result       |
   |----------|----------|--------------|
   | Rock     | Rock     | Tie          |
   | Rock     | Scissors | Player 1     |
   | &nbsp; | | |
   | &nbsp; | | |
   | &nbsp; | | |

2. **Create the Program**:
   - Create a new file in the `05_2_homework` directory named `rps.py` that will generate the outcome of the rock, paper, scissors game.
   - The program should ask the user for input and display the answer as follows:
     ```
     Player 1? rock
     Player 2? scissors
     Player 1 wins.
     ```
   - The only valid inputs are `rock`, `paper`, and `scissors`. If the user enters anything else, your program should output:
     ```
     This is not a valid object selection
     ```
   - Use the truth table you created to help with creating the conditions for your `if` statement(s).

### Notes
- If you have a long condition in your `if` statement and want to split it into multiple lines, you can either enclose the entire expression in parentheses, e.g.:
  ```python
  if (player1 == 'rock' and 
      player2 == 'scissors'):
      print('Player 1 wins.')
  ```
- Or, you can use the backslash symbol to indicate to Python that the next line is still part of the previous line of code, e.g.:
  ```python
  if player1 == 'rock' and\
     player2 == 'scissors':
      print('Player 1 wins.')
  ```
- Use whichever form you feel comfortable using.
