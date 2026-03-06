# Cache Eviction Policy Simulator

Gabriel Burger -- 89739553
CJ Alexander -- 51691777

## How to Run

Python must be installed.

```
python3 src/cache_simulation.py <input_file>
```

Example:
```
python3 src/cache_simulation.py data/example.in
```

Input file has two lines first line is `k m` (cache size and number of requests), second line is the request sequence. Output prints the miss count for each policy.

## Files

```
src/
  cache_sim.py   -- main program, reads input and runs all three policies
  fifo.py        -- FIFO cache (set + deque)
  lru.py         -- LRU cache (OrderedDict)
  optff.py       -- Belady's optimal (precomputed next-use)
data/
  example.in     -- small example (k=2, 8 requests)
  example.out    -- expected output
  tests/
    test1.in     -- cyclic pattern, k=3, 50 requests
    test1.out
    test2.in     -- locality pattern, k=4, 60 requests
    test2.out
    test3.in     -- pattern showing LRU > FIFO, k=3, 50 requests
    test3.out
writeup.md       -- written answers
```
