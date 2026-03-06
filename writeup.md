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

### Question 2: Bad Sequence for LRU (k=3)

We used `1 2 3 4 1 2 3 4 1 2 3 4` with k=3.

LRU: `1 2 3` are 3 cold misses. Then `4` comes in, evict 1 (least recent), `1` comes in, evict 2, `2` comes in, evict 3, and so on. We're always evicting exactly the item that's about to be requested next. LRU misses on every request 12 out of 12.

OPTFF: Same 3 cold misses for `1 2 3`. When `4` arrives, OPTFF looks ahead and sees 1 is needed at pos 4, 2 at pos 5, 3 at pos 6 so it evicts 3 (farthest away). Then `1` is a hit, `2` is a hit. When `3` comes back it evicts 2 (farthest future use). `4` hit, `1` hit. Only 6 misses total.

So OPTFF gets 6 vs LRU's 12. LRU is not performant with this pattern because with 4 items cycling through a size-3 cache it always kicks out exactly what we need next. OPTFF doesn't have that problem since it knows the future.

### Question 3: Proof that OPTFF is Optimal

Let's say we have our OPTFF algorithm, and any algorithm A that processes the same request sequence with cache size k.

At some point, because the algorithms are different there will be an eviction point because of a cache miss. Up until this point, everything before this point must be identical.

The OPTFF algorithm will evict the item whose next use is farthest in the future. Let's call this y. The algorithm will choose an item based on whatever policy it has. Let's call this x. We will also create a modified version of A called A', that chooses to evict y instead of evicting x. At this point, A and A' are exactly the same, besides just differing by one item.

Eventually, one of two things will happen. It's either x gets requested and A will have a cache miss, while A' won't. A' is more performant in this case. Or y gets requested and A' will have a cache miss, while A won't, making A more performant in this case.

However because OPTFF specifically chose y as the farthest future item, it is guaranteed that x will be requested before y in the sequence. Therefore, at this step misses(A') <= misses(A).

If there are future disagreements, we can apply this argument at each one. Because there are only a finite number of requests in a sequence, that means there is a finite number of possible disagreements. The process must eventually end.

To conclude, because we can take any algorithm A and transform it into OPTFF without increasing misses, no other algorithm can perform better. So, OPTFF must be optimal.
