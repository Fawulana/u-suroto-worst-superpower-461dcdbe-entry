[![make.fun · u-suroto-worst-superpower-461dcdbe](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-worst-superpower-461dcdbe)
[![rank](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/Fawulana/u-suroto-worst-superpower-461dcdbe-entry/rank.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-worst-superpower-461dcdbe)
[![reward](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/Fawulana/u-suroto-worst-superpower-461dcdbe-entry/reward.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-worst-superpower-461dcdbe)

# Worst Superpower

Entry for the [Worst Superpower bounty](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe) on make.fun: invent the most useless superpower in one line of at most 140 characters.

## The line

> I can sense the exact second any microwave finishes cooking — but only other people's, and only once the beeping has already stopped.

Why this line: the power sounds grand ("sense the exact second any microwave finishes") until the double limitation lands — it only works on *other people's* microwaves, and only *after* the beep you could already hear yourself. It is genuinely useless (it helps no one, not even its owner), instantly picturable (a hero standing in a kitchen, solemnly sensing a stranger's popcorn across town), and specific enough to be funny on a single reading.

## How it works

`main.py` (Python 3.13, stdlib only) writes the line to `/output/entry.txt` with no trailing newline. It is fully deterministic and offline — no network, no environment reads, no randomness — so every run produces the exact same bytes. Before writing it validates the gate: 1–140 characters, a single line, not whitespace-only; after writing it re-reads the file and checks it matches the line exactly.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
