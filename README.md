# Multi-Agent Tic-Tac-Toe

A Tic-Tac-Toe game with four AI opponents and a head-to-head comparison tool, built with Python and Tkinter.

## AI Models

**Statistical** — Scores each move by win-minus-loss frequency across all pre-enumerated game continuations from the current board state. Adds a block/instant-win override on top.

**Minimax** — Full game-tree search. Unbeatable. First move is hardcoded to center to avoid slowdown.

**Random** — Picks a random available cell.

**Q-Learning** — Two agents trained via self-play: one for moving first (`agent_x.pkl`), one for moving second (`agent_o.pkl`).

## Comparison Tool

Select any two models, simulate 100 games headlessly, see win/draw percentages. Accessible from the model selection screen.

## Requirements

```
pip install playsound3
```

## Run

```
python main.py
```
