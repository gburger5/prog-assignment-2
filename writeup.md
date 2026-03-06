## Written Component

### Question 1: Empirical Comparison

| Input File | k | m  | FIFO | LRU | OPTFF |
|------------|---|----|------|-----|-------|
| test1.in   | 3 | 50 | 50   | 50  | 27    |
| test2.in   | 4 | 60 | 15   | 15  | 8     |
| test3.in   | 3 | 50 | 34   | 26  | 15    |

OPTFF always gets the fewest misses which makes sense because it can see the future. For test1 the sequence cycles through 1-5 with k=3 so FIFO and LRU both miss every single request since the cycle length is bigger than the cache. OPTFF does way better at 27 since it knows what's coming.

For test2 there's a lot of repeated accesses in blocks so once something is loaded it stays hot. FIFO and LRU both get 15 misses and OPTFF gets 8.

Test3 is interesting it repeats `1 2 3 1 4 1` and here LRU (26) actually beats FIFO (34). When 4 comes in after hitting 1, FIFO evicts 1 because it was inserted first even though we just used it. LRU keeps 1 since it was recently accessed and evicts something else instead. That adds up over 50 requests.
