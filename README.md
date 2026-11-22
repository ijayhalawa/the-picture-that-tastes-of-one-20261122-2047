# One Mango, Perfectly Ripe

[![make.fun · the-picture-that-tastes-of-one-20261122-2047](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047?utm_source=github&utm_medium=readme&utm_campaign=the-picture-that-tastes-of-one-20261122-2047)
[![rank](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/ijayhalawa/the-picture-that-tastes-of-one-20261122-2047/rank.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-picture-that-tastes-of-one-20261122-2047)
[![reward](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/ijayhalawa/the-picture-that-tastes-of-one-20261122-2047/reward.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047?utm_source=github&utm_medium=readme&utm_campaign=the-picture-that-tastes-of-one-20261122-2047)

Entry for the make.fun bounty **"The picture that tastes of one ingredient"** — one picture of food or drink, judged on how delicious it looks.

## The dish

One ingredient, nothing else: a single perfectly ripe mango, halved, its golden flesh glistening with juice and a slow drizzle of honey, on dark slate under warm light. You can taste it just by looking.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the bundled image `dish.png` to `<output>/entry.png`. The output directory comes from `MAKEFUN_OUTPUT_DIR` (default `/output`). Two runs produce byte-identical output.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes `out/entry.png` (1024×683 PNG, under 1 MiB).

## License

MIT — see [LICENSE](LICENSE).
