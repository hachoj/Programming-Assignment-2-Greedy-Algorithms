## Question 1: Empirical Comparison

Use **at least three nontrivial input files** (each containing 50 or more requests).

For each file, report the number of cache misses for each policy.

| Input File | k  | m | FIFO | LRU | OPTFF |
|------------|----|---|------|-----|-------|
| File1      | 5  | 50 |  35  | 38  |  23   |
| File2      | 10 | 75 |  61  | 61  |  37   |
| File3      | 3  | 100|  94  | 94  |  50   |

Briefly comment:

- Does OPTFF have the fewest misses?

Yes, OPTFF accross all three tests, has the fewest misses.

- How does FIFO compare to LRU?

FIFO has no significant difference in the amount misses compared to LRU.
 
---

## Question 2: Bad Sequence for LRU or FIFO

For ( k = 3 ), investigate whether there exists a request sequence for which OPTFF incurs **strictly fewer misses** than LRU (or FIFO).

- If such a sequence exists:
  - Construct one.
  - Compute and report the miss counts for both policies.
- If you believe no such sequence exists for the policy you chose:
  - Provide a clear justification.

In either case, briefly explain your reasoning.

Yes, a sequence like this exists. For cache size k=3, one example request sequence is 1,2,3,4,1,2,5,1,2,3,4,5.
For this sequence OPTFF incurs 7 misses while LRU incurs 10 misses, and the reason for this is that OPTFF knows
the future request sequence and always evicts the item whose next use is farthest in the future. This means that
it avoids evicting values that will be needed again soon. On the other hand, LRU only uses past information and evicts
the least recently used item even if that item is about to be requested again. In this sequence, that causes LRU to
make worse eviction choices and leads to more misses. As a result, this example shows that for k=3 there does exist a
sequence where OPTFF has fewer misses than LRU. 

---

## Question 3: Prove OPTFF is Optimal

Let OPTFF be Belady's Farthest-in-Future algorithm.

Let ( A ) be any offline algorithm that knows the full request sequence.

Prove that the number of misses of OPTFF is no larger than that of ( A ) on any fixed sequence.

