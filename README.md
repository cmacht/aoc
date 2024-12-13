# aoc2024
https://adventofcode.com/2024

## Daily Reflections

### 01 - number comparison
I only started at 6:32am but then managed to solve the problem in 8min + 4min, using
[`zip()`](https://docs.python.org/3.3/library/functions.html)
to iterate over two lists at the same time.

### 02 - number comparison
I remembered `itertools.pairwise` and managed to score rank 6800 on part one.
Part two was hard for me, as I tried to get clever and work only with a list of deltas.

### 03 - string, regex
Hilariously, this was one of my more successful days in terms of speed.
I committed right away to a long list of conditionals, checking character-by-character resulting
in some of [the worst code I've ever written](https://github.com/cmacht/aoc/blob/main/03/puzzle03.py).

As it turns out, the regex would not have been too hard and I would have been faster,
even if I had spent the time to look it up. I agree with the sentiment voiced on a
[StackOverflow answer](https://stackoverflow.com/a/1098336):
"Professional developers should be familiar with basic regex syntax."
but do also concur with dappy's statement that "regex are a great use case for llms".

Google searches for "regex" apparently also spiked in the morning.

### 04 - grid, transpose
I felt confident writing an algorithm that took the grid and looked for "XMAS" line by line,
then transposing the grid for the vertical search and reusing my function.
But hit a roadblock when I realised that I wasn't able to rotate the grid 45deg for diagonal searching.
I then copied [HyperNeutrino's] solution that searches char-wise in 8 directions instead of line-wise.

### 05 - sorting
Last one that I managed to complete in the morning. (edit: or so I thought. P2 of day2 was also late.) Instructions seemed convoluted at first.
In part two, I implemented a very stupid sorting algorithm.

- [ ] Improve [sorting algorithm](https://github.com/cmacht/aoc/blob/1130b465c3e7049763365930c9d2736db9b84438/05/puzzle05b.py#L23)

### 06 - grid, pathfinding
I was happy with my solution, as it looked clean and straight-forward and solved `input-training`.
Frustratingly, it failed with the full `input`. Thanks to [Papierkorb's](https://github.com/Papierkorb2292)
suggestion to try and modify the test input first, 
I figured out that this was due to an incorrect check for boundaries, which I fixed [in this commit](https://github.com/cmacht/aoc/commit/872294b51cf749d0d12b40039d347ee4dcbb08ac#diff-acf549eb5923d4256cd93615abdeaee28f71c5c61b208e8cf87df4bc4eed9deeR40).

I thought long on how to best implement a "finding loops" algo: I first thought of checking the coords for closed rectangles,
but then settled on something I called "shoot right", where I would check for possible turning edges on a 90deg angle from the guard,
as rejoining them would possibly mean, that he falls back in the same pattern. I could not get it to work though
and settled on a brute force approach that I copied from HyperNeutrino's solution.
- [x] [HyperNeutrino](https://youtu.be/UPS2jl3JmCs?t=369) has a clever short solution for turning right.

### 07 - math, brute force, binary tree?, backwards?
This day was the most annoying grind, as I got stuck on how to generate all number combinations.
I needed to use `itertools.product`(), which I was not familiar with,
as it covers more combinations than `itertools.combinations`.
Once Christer pointed me to it, and it clicked for me, implementation was fine and part two surprisingly simple.

- [x] There's a clever idea by [HyperNeutrino](https://www.youtube.com/watch?v=1ZIJ9qo9bnY) who approaches the list backwards.
- [ ] I was also wondering if instead of brute forcing through all combinations, a binary tree (?) would make sense. How to implement it?

### 08 - grid, vectors
Nice. Instructions were a bit obscure (what is an "antinode"?) but the examples made it clear.
Writing down on paper what I would do with the vectors & delta vector helped.
Also had to utilise [`itertools.combinations`](https://docs.python.org/3/library/itertools.html#itertools.combinations)

### 09 - defragmentation
I think I was quite happy with my first solution, but then tried to get too clever with part two
and only use the deltas between numbers, which turned out to be more difficult than just going through
the list. I left this one for 4 days (also had a pretty bad cold) and then solved it quite concisely
once I felt better.

### 10 - grid, pathfinding
Not as easy as I thought: I tried to solve the search recursively but couldn't and then accidentally messed
up my input. I used BFS, and went back to a [resource for pathfinding](https://www.redblobgames.com/pathfinding/grids/graphs.html)
I had found last year, wasn't needed. Seeing [HyperNeutrino's](https://youtu.be/layyhtQQuM0?t=136) implementation
proved to be much more clear.

Amazingly, part two required only a change of 5 characters, from `set()` to `[]`.

### 11 - big numbers?


## Learning
- Use `row` and `column` instead of `x-axis` and `y-axis` because `grid[r][c]` is more intuitive/less confusing than `grid[y][x]`
- If you need indices, it's better to use `for i in range(len(grid)):` than `for idx, el in enumerate(lines):`
- `set()` often becomes important to eliminate duplicates in answers
- if `input-training` works but `input` doesn't, try with a modified `input-training` first (day6)
- `map(int, num.split(','))` only works with a surrounding `list(...)` not `[...]`, which returns a `map object` (day2).
Papierkorb explained: "`map()` returned einen iterator, den man mit `list()` umwandeln kann."