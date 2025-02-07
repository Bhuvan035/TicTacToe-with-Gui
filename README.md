# TicTacToe with GUI

## Overview
TicTacToe with GUI is a simple multiplayer Tic-Tac-Toe game built using **Python's Tkinter** for the graphical interface and **sockets** for network communication. The game allows two players to compete over a network connection.

## Features
- **Graphical User Interface (GUI)** using Tkinter.
- **Multiplayer support** via socket programming.
- **Game statistics tracking**.
- **Cross-platform compatibility** (built on Windows but can run on other OS with Python installed).

## Installation
### Prerequisites
Make sure you have Python installed on your system. You can download it from:
[Python Download](https://www.python.org/downloads/)

## How to Play
### Step 1: Start the Server and Client
- Run `player2tk.py` first, as it acts as the **server**.
```sh
python player2tk.py
```
- Run `server1tk.py`, which will act as the **client**.
```sh
python server1tk.py
```

### Step 2: Establish Connection
- On **player2tk.py (server)**, enter the connection details (IP address and port number) and submit.
- On **server1tk.py (client)**, enter the same connection details and submit.
- Once both are connected, the game will begin automatically.

## Game Rules
- The game follows standard Tic-Tac-Toe rules.
- Player 1 (Server) and Player 2 (Client) take turns.
- The first player to align three marks (X or O) in a row, column, or diagonal wins.
- The game ends in a **draw** if the board is full with no winner.

## Future Improvements
- Add AI opponent for single-player mode.
- Enhance UI/UX with animations and better graphics.
- Implement game history and leaderboard.

## Contact
For any questions or issues, reach out via GitHub Issues or email me at **bhuvanchandra3008@gmail.com**.

