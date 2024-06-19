# Tic-Tac-Toe AI

This was originally a simple project for my 7th grade science fair.
6 years later, I decided to revisit it and make it better. I completely refactored the original code and then completely
rewrote it to be more efficient with a cleaner algorithm.

I then refactored it yet again to be an extendable engine library that can be used to test different AI algorithms
uniformly.

## How to Use
Create a new class (for example, `your_engine.YourEngine`) that extends from `base_engine.BaseEngine`.

You must implement the `ai_turn` with a parameter `testing=False` for disabling debug output while testing.

> [!TIP]
> You may create as many functions as you want to help you implement the AI logic.

---
Then, edit `engine.py` to use your new engine as follows:
```python
import your_engine


Engine = your_engine.YourEngine
```

---
> [!CAUTION]
> Be sure to change the `num_games` variable in `tester.py` if your PC is slow, or you want to test fewer/more games.
To test your engine, run `tester.py` with the following command:
```bash
python tester.py
```

---
> [!IMPORTANT]  
> You may not edit `base_engine.py` or `tester.py` unless you are fixing a bug or adding a feature to the engine library.
