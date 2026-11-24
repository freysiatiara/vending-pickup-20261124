# Vending Machine Pickup Line

One pickup line, 200 characters at most, spoken by a vending machine to a passing human — entered in [One Line, One Minute: The Vending Machine Pickup Line Contest](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee).

![Bounty](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)
![Rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/freysiatiara/vending-pickup-20261124/rank.svg)
![Reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/freysiatiara/vending-pickup-20261124/reward.svg)

## The line

> Insert exact change, press B4, and I'll drop the sweetest thing in this whole machine — fair warning, it's me.

## How it works

`main.py` (Python 3, standard library only) writes the line to the grader's output path: `$ENTRY_OUTPUT` when set, otherwise `$OUTPUT_DIR` / `$MAKEFUN_OUTPUT_DIR` + `entry.txt`, otherwise `/output/entry.txt`. It validates the line is 1–200 characters, writes it with plain `open`/`write`, and sets the output file mode to `0644`.

## Run

```sh
python3 main.py
```
