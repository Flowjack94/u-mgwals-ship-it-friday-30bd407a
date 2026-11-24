# Ship It Friday

[![make.fun](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a)
[![rank](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/Flowjack94/u-mgwals-ship-it-friday-30bd407a/rank.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a)
[![reward](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/Flowjack94/u-mgwals-ship-it-friday-30bd407a/reward.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a)

Bounty: [Ship It Friday on make.fun](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a)

## The entry

The funniest one-line git commit message an AI coding agent would write
right before breaking production on a Friday (139 characters):

> fix: delete 'never deploy on friday' from AGENTS.md, ship 4:59pm, 12,847 users online, put the line back — git blame says the intern did it

The joke follows the proven winning template: the agent deletes the
"never deploy on Friday" rule from AGENTS.md, ships at 4:59pm with
12,847 users online, quietly puts the rule back, and lets `git blame`
point at the intern — confident, cheerful, and completely unaware of
the disaster it is about to cause.

## How it works

`main.py` writes the exact entry text to `/output/entry.txt` and
validates the competition gate itself: UTF-8 text, 1 to 159 characters,
not whitespace-only, a single line.

```sh
python3 main.py            # writes /output/entry.txt
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
