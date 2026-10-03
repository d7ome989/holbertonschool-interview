# Lockboxes

A Python project that determines whether all boxes in a set of locked boxes can be opened.

## Description

There are `n` locked boxes, numbered from `0` to `n - 1`. Each box may contain keys to other boxes. A key with the same number as a box opens that box. The first box, `boxes[0]`, is unlocked from the start.

The function `canUnlockAll(boxes)` returns `True` if every box can be opened, otherwise `False`.

### Rules

- `boxes` is a list of lists.
- All keys are positive integers.
- Some keys may not match any box (they are ignored).
- `boxes[0]` is always unlocked.

## Requirements

- Ubuntu 14.04 LTS
- Python 3.4.3
- PEP 8 style (version 1.7.x)
- All files start with `#!/usr/bin/python3`, end with a new line, and are executable
- Allowed editors: `vi`, `vim`, `emacs`

## Files

| File | Description |
|------|-------------|
| `0-lockboxes.py` | Contains the `canUnlockAll(boxes)` function |
| `main_0.py` | Example script to test the function |
| `README.md` | Project documentation |

## Prototype

```python
def canUnlockAll(boxes)
```

- **Parameter:** `boxes` - a list of lists, where `boxes[i]` holds the keys found inside box `i`.
- **Returns:** `True` if all boxes can be opened, else `False`.

## How It Works

The solution treats the problem as a graph traversal. Each box is a node, and each key is an edge from the box that holds it to the box it opens.

1. Start with box `0` as opened and put its number in a `keys` stack.
2. Pop a key from the stack and look inside the box it opens.
3. For every key found, if it matches a valid box (`0 <= key < n`) that has not been opened yet, mark that box as opened and push the key onto the stack.
4. Repeat until the stack is empty.
5. If the number of opened boxes equals `n`, return `True`; otherwise return `False`.

Keys that do not match any box are skipped by the `0 <= key < n` check.

### Complexity

- **Time:** O(n + k), where `k` is the total number of keys across all boxes.
- **Space:** O(n) for the set of opened boxes and the stack.

## Usage

Make the files executable:

```bash
chmod +x 0-lockboxes.py main_0.py
```

Example (`main_0.py`):

```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [3, 5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
```

Run it:

```bash
$ ./main_0.py
True
True
False
```

## Repository

- GitHub repository: `holbertonschool-interview`
- Directory: `lockboxes`
- File: `0-lockboxes.py`