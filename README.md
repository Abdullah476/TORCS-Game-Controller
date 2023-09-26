# TORCS-Game-Controller

## Overview

This repository contains an AI-driven controller for the TORCS (The Open Racing Car Simulator) game, implemented in Python. The controller leverages machine learning techniques to make decisions for the in-game car, allowing it to navigate the track and compete against other AI or human-controlled cars.

## Installation

To use this controller, you need to follow these steps:

**Clone the Repository:**

   ```
   git clone https://github.com/Abdullah476/TORCS-Game-Controller.git
   ```

## Usage

1. **Start TORCS:**

   Before running the AI controller, make sure you have TORCS installed on your system. You can download TORCS from [http://torcs.sourceforge.net](http://torcs.sourceforge.net).

   Start TORCS and select a race track.

2. **Run the AI Controller:**

   ```
   python driver.py
   ```

   This command will start the AI controller, which will connect to the TORCS server, receive game state information, make decisions, and send control commands to the in-game car.

3. **Watch the AI in Action:**

   You can now watch the AI-controlled car compete in the selected race. The AI uses a Decision Tree Regression model to make decisions, which has been trained on a dataset of various game scenarios.

## Models

Multiple machine learning models were trained to make decisions for the AI controller. The uploaded model in this repository is based on Decision Tree Regression.

## Training

If you wish to train your own models or modify the existing ones, you can find the training data and scripts in the directory.

## Contributing

If you would like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Contributions such as improving AI decision-making algorithms, adding new models, or enhancing the codebase are welcome.

## Issues and Bug Reports

If you encounter any issues or find any bugs in the AI controller, please report them on the GitHub issue tracker.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This AI controller was developed as part of a project.
- Special thanks to the TORCS community for providing the racing simulator and resources for AI development.

Enjoy racing with your AI-driven controller in TORCS!


