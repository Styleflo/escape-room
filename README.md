# Escape Room - Quandela Aptitude Test

This repository contains my implementation of a Python class representing a room in an escape game, created for the Quandela technical aptitude test.

## Overview

The goal of this script is to provide a clean, Object-Oriented approach to a text-based escape room logic. Rather than relying on complex external managers or player classes, the `Room` class handles its own state, connections, and locks, while utilizing a simple shared state for the player's inventory.

## Instruction

Write a Python class representing a room in an escape game. Rooms may contain objects, keys, and doors leading to other rooms. Implement methods to:
* move between rooms,
* pick up and use items, 
* unlock doors, 
* display the current state of the game.

Ensure that instances of your class produce human-readable output when using print(). Additionally, provide code to test your class functions and adhere to the [PEP 8 – Style Guide](https://peps.python.org/pep-0008/) for Python Code.


## Features

The `Room` class implements the following required mechanics:
*   **Navigation:** Move between different connected rooms (`move`).
*   **Item Management:** Pick up items found in rooms and store them in the inventory (`pick_up`).
*   **Interaction:** Use items from the inventory to interact with the environment, specifically to unlock doors (`use_item`).
*   **State Display:** A human-readable terminal output displaying the current room's description, visible items, available exits (and their lock status), and the player's inventory (`__str__`).

## How to Run

You can run the simulation script directly from your terminal. It includes a built-in test flow that demonstrates the core mechanics.

```bash
python3 escape_room.py
```

## Author
**Florian Touraine**
