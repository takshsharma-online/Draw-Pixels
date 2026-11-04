_# Draw-Pixels - Game Overview_

Draw Pixels is a two-player digital Pictionary game application developed using Python and the PyQt6 framework. The game is based on the traditional Pictionary concept, where one player communicates a word through drawing while the other player attempts to identify it.

The main objective is to guess the correct word based on the illustration within a limited amount of time. The game combines creativity, visual communication and problem-solving to create an entertaining and interactive experience.

_**How the game Works?**_

**1. Starting the game**
When the application launches, players are presented with a home screen where they can start a new game, view the instructions or exit the application.

**2. Entering the Word**
At the beginning of each round, the first player is prompted to enter a word or phrase they want the other player to guess. The entered word is kept hidden from the guessing player to ensure fairness.

**3. Drawing Phase**
Once the word has been entered, the drawing player is presented with a blank digital canvas. They must illustrate the chosen word without writing any letters, numbers or the actual word.

The application provides drawing tools such as:

* Pencil for freehand drawing.
* Eraser for removing unwanted strokes.
* Colour palette for selecting different colours.
* Clear canvas to restart the drawing.

A countdown timer begins when the drawing phase starts. The player must complete their illustration before the allocated time runs out.

**4. Guessing Phase**
Once the drawing player finishes or the timer expires, the application moves to the guessing phase.

The second player is shown the completed drawing and is given an opportunity to identify the word. They enter their guess into a designated text box, and the application checks whether it matches the original word.

**5. Scoring System**
Points are awarded when the guessing player correctly identifies the word.

If the player fails to guess correctly, no points are awarded for that round. The application displays the round result and updates the scoreboard accordingly.

**6. Switching Players**

After a round is completed, the players switch roles. The previous drawing player becomes the guesser, while the previous guesser gets to enter a new word and create the next illustration.

This ensures that both players have an equal opportunity to draw and guess.

**7. End of Game**

The game continues for a predetermined number of rounds. Once all rounds are completed, a results screen displays the final scores and announces the winner.

Players can then choose to start a new game or return to the main menu.

**_Overall Objective_**
The purpose of Draw Pixels is to provide an enjoyable two-player gaming experience that encourages creativity, imagination and visual communication.

By allowing players to create their own words and illustrations, the game offers a more personalised experience than traditional word-guessing games. The application also demonstrates the use of Python and PyQt6 in developing graphical user interfaces, handling mouse interactions, implementing timers, managing game states and processing user input.