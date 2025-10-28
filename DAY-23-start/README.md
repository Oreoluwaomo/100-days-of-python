Project Goal:
Build a fully functional Turtle Crossing Game, inspired by the classic “Frogger.”
The player controls a turtle that must safely cross a road filled with moving cars.
Each time the player reaches the other side, the game increases in difficulty by speeding up the cars.

This project is an excellent capstone for learning Object Oriented Programming (OOP), event driven logic, and collision detection using the turtle module.
What I Built

Player Class (player.py):
Created a turtle-shaped player that starts at the bottom of the screen.
Moves forward each time the Up arrow key is pressed.
Automatically resets its position upon reaching the finish line (top of the screen).

CarManager Class (car_manager.py):
Dynamically generates cars at random intervals and y-positions.
Cars move from the right to the left side of the screen continuously.
Each car’s color is randomly chosen from a predefined color list.
The speed of all cars increases each time the player levels up.

Scoreboard Class (scoreboard.py):
Displays the current level at the top-left corner of the screen.
Updates the level every time the player successfully crosses the road.
Shows a “GAME OVER” message when a collision is detected.

Main Game Loop (main.py):
Coordinates interactions between all classes.
Continuously updates the screen to animate movement.
Detects collisions between the player and cars using the distance() method.
Pauses the loop and ends the game when the player collides with a car.

Concepts Practiced

Object-Oriented Programming (OOP)

Designed multiple classes (Player, CarManager, Scoreboard) with encapsulated logic.

Created interactions between class instances in the main loop.

Event Listeners & Key Binding

Used screen.listen() and screen.onkey() to control player movement in real time.

Collision Detection

Used the distance() method to detect when the player and a car are too close.

Dynamic Object Creation & Management

Created and stored multiple car objects in a list for continuous animation and deletion.

Speed Scaling & Game Progression

Increased car speed each time the player reached a new level, adding difficulty.

Screen & Animation Management

Controlled refresh rate using time.sleep() and screen.update() for smoother animation.

Summary

Day 23’s Turtle Crossing Capstone Project was a major step forward in mastering OOP and interactive Python programming.
It required combining everything learned so far from classes and attributes to animation timing, user input, and collision detection.

By the end of the project, I understood:

How multiple classes interact dynamically within one program.

How to build games with real time feedback using the turtle module.

How to manage difficulty progression and maintain clean code structure across multiple files.

This project marked the point where Python became more than syntax ,it became a tool to build interactive experiences.
