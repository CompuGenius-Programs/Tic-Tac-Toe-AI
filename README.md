# Tic-Tac-Toe AI

This project started as a simple endeavor for my 7th grade science fair. Six years later, I've revisited it to enhance
and refine the original code. The result is a more efficient and elegantly structured algorithm. I've further refactored
the project into an extendable engine library, allowing for uniform testing of various AI algorithms.

## How to Play the Game
To play the game, run
```bash
python engine.py
```
which will use `new.NewEngine` by default, but you can edit to it use `old.OldEngine` or a brand new one you create
(instructions below)!
You can also play the original version created 6 years ago (although slightly cleaned up) by running
`original_pygame.py`.

## How to Use the AI Engine Library

To create your own AI engine, follow these steps:

1. Create a new class (e.g., `your_engine.YourEngine`) that extends `base_engine.BaseEngine`.
2. Implement the `ai_turn` method, with a parameter `testing=False` to disable debug output during testing.

> [!TIP]
> Feel free to create additional functions to assist with your AI logic implementation.

---

3. Next, modify `engine.py` to use your new engine by adding the following code:

```python
import your_engine

Engine = your_engine.YourEngine
```

---

> [!CAUTION]
> Adjust the `num_games` variable in `tester.py` according to your computer's performance. This will allow you to test
> fewer or more games as needed.

4. To test your engine, run `tester.py` with the command:

```bash
python tester.py
```

---

> [!IMPORTANT]
> Do not edit `base_engine.py` or `tester.py` unless you are fixing a bug or adding a feature to the engine library.


## File Directory
### Engine Library
- `base_engine.py`: Contains the base engine class that all AI engines must extend.
- `tester.py`: Contains the testing logic for the AI engine.
- `engine.py`: Contains the engine class that the tester uses.
---
### AI Engines
- `original_pygame.py`: A barely cleaned-up version of the original code from the 7th grade science fair project. _Not
compatible with the engine library._
- `original_cli.py`: A cleaned-up version of the original code from the 7th grade science fair project. _Not compatible
with the engine library._
- `original.py`: A port of `original_cli.py`. _Compatible with the engine library._
- `new.py`: A complete rewrite of the original code using cleaner and more efficient logic. _Compatible with the engine
library._


## License
This project is licensed under the GNU General Public License v3.0. For more information, see the `LICENSE` file.