# Prime Game

## Description

Maria and Ben are playing a game with the set of consecutive integers from `1`
to `n`. They take turns choosing a prime number from the set and removing that
number and its multiples. The player who cannot make a move loses the round.

They play `x` rounds, where `n` may be different in each round. Maria always
goes first and both players play optimally. The program determines who won the
most rounds.

## Requirements

* Prototype: `def isWinner(x, nums)`
* `x` is the number of rounds and `nums` is an array of `n`
* Returns the name of the player who won the most rounds
* Returns `None` if the winner cannot be determined
* `n` and `x` are not larger than `10000`
* No packages are imported

## How It Works

Choosing a prime removes its multiples, but it never removes another prime.
So each turn removes exactly one prime, and the number of turns in a round
equals the number of primes between `1` and `n`.

| Number of primes | Winner |
|------------------|--------|
| Odd              | Maria  |
| Even (including 0) | Ben  |

### Functions

| Function                    | Role                                            |
|-----------------------------|-------------------------------------------------|
| `count_primes_up_to(limit)` | Lists the number of primes up to each number    |
| `isWinner(x, nums)`         | Plays the rounds and returns the overall winner |

The primes are found with the Sieve of Eratosthenes, once, up to the largest
`n`. Each round then reads its prime count directly from the list.

## Usage

`main_0.py`:

```python
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
```

Output:

```
$ ./main_0.py
Winner: Ben
```

## Repository

* GitHub repository: `holbertonschool-interview`
* Directory: `primegame`
* File: `0-prime_game.py`

## Author

Abdulrhman Saleh Alduqil (d7ome989)