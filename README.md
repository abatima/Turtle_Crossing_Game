# Turtle Crossing Game 🐢

A fast-paced "Frogger-style" arcade game built using **Python** and the **Turtle** graphics library. This project focuses on managing multiple moving objects, collision detection, and level-based difficulty scaling.

## 🎮 Features

* **Infinite Leveling:** Every time you reach the finish line, the level increases and the cars move faster.
* **Randomized Traffic:** Cars are generated at random intervals and in random colors along the y-axis.
* **Collision Logic:** The game ends immediately if the turtle collides with any of the moving cars.
* **Dynamic Scoreboard:** Tracks your current level at the top of the screen.
* **Smoothed Animations:** Uses screen update management to handle dozens of moving objects simultaneously.

## 🛠️ Built With

* [Python 3](https://www.python.org/)
* `turtle` module (built-in Python graphics)

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.x installed. Verify your version by running:

```bash
python --version

```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/abatima/Turtle_Crossing_Game.git

```


2. Navigate to the project directory:
```bash
cd Turtle_Crossing_Game

```



### Running the Game

Start the game by running the main script:

```bash
python main.py

```

## 🕹️ How to Play

Guide the turtle from the bottom of the screen to the top while avoiding the oncoming traffic.

### Controls

| Action | Key |
| --- | --- |
| **Move Up** | `Up Arrow` |

## 📂 File Structure

* `main.py`: The main game loop. It coordinates the player movement, car generation, and collision checking.
* `player.py`: Contains the `Player` class, defining the turtle's starting position, movement, and finish line detection.
* `car_manager.py`: Manages the generation, movement, and speed increases of all car objects on the screen.
* `scoreboard.py`: Handles the level display and the "Game Over" sequence.

## 📜 License

This project is open-source and available under the [MIT License](https://en.wikipedia.org/wiki/MIT_License).

## 🤝 Contributing

Contributions are welcome! You could enhance the game by adding:

* Horizontal movement for the turtle.
* Different types of vehicles with varying speeds.
* A "Lives" system instead of instant Game Over.

---

*Created by [abatima*](https://github.com/abatima)
