Harrison Chojnowski: `46524954`

Pranav Annapareddy: `21340719`

**Running our code:**

Create a conda/mamba env or venv with python>=3.9

Once that environment is active, run,

pip install -e
from the project root.


---


The default behavior of our project is to use `data/data.in` and `data/data.out` to test for the number of cache misses for FIFO/LRU/OPTFF. 

There are two optional flags: `-i/--input` and `-o/--output`. They let you specicy furhter input and output file paths. If the input path is invalid, the program will return an error. If the output path is invalid but the input path is valid, the program will still run, ommitting the outputs.

EX:
```bash
python main.py

python main.py -i data/data2.in

python main.py -i data/data2.in -o data/data2.out

python main.py -i data/not_real_path -o data/data.out # Error

python main.py -i data/data.in -o data/not_real_path # Runs without output
```

**Assumptions:**

The `data.in` format should be:
```
k m
r1 r2 ... rm
```
where `k` is the cache capacity, `m` is the number of cache requests, and `r1 ... rm` are those cache requests in order.

The `data.out` format should be:
```
a
b
c
```
where a is the correct number of misses, given the `data.in` for FIFO, `b` is the same but for LRU, and `c` is the same but for OPTFF.

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

Proof: Follows directly from the following *invariant*.

*Invariant*: There exists an optimal reduced schedule $S$, that has the same eviction schedule as $S_{FF}$ through the first $j$ steps.

Base Case: $j = 0$.
Let $S$ be a reduced schedule that satisfied invariant through $j$ steps.

We produce $S'$ that satisfies invriant after $j + 1$ steps.
- Let $d$ denote the itme requested in step $j + 1$.
- Since $S$ and $S_{FF}$ have agrred up until now, they have the same cache contents before step $j + 1$.
- Case 1: $d$ is already in cache.
	- $S' = S$ satisfies invariant.
- Case 2: $d$ is not in the cache and $S$ and $S_{FF}$ evict the same item.
	- $S' = S$ satisfies invriant.
- Case 3: $d$ is not in cache; $S_{FF}$ evicts $e$; $S$ evicts $f \neq e$.
	- begin contruction of $S'$ from $S$ by evicting $e$ instead of $f$.
	- now $S'$ agrees with $S_{FF}$ for the first $j+1$ steps: we show that having item $f$ in cache is no worse than having item $e$ in cache.
	- let $S'$ behave the same as $S$  until $S'$ is forced to taken a different action (because either $S$ evicts $e$; or because $e$ or $f$ is requested)
	- Let $j'$ be the first step after $j+1$ that $S'$ must take a different action from $S$; let $g$ denote the item requested in step $j'$.
	    - involves either $e$ or $f$ (or both)
	- ***Just for reference $S$'s cache contains $e$ but not $f$, while $S'$ and $S_{FF}$ contain $f$ but not $e$.***
	- Case 3a: $g = e$.
		- If $g = e$ then $S$ is a hit while $S'$ is a miss, but this is a contradiction, because if $e$ was needed before $f$, then $S_{FF}$ would have ejected $f$ rather than $e$.
	    - So $S'$ agrees with $S_{FF}$ through first $j+1$ steps.
	- Case 3b: $g = f$.
	    - Element $f$ can't be in cache of S; let $e'$ be the item that $S$ evicts.
		- if $e' = e$, $S'$ accesses $f$ from cache; now $S$ and $S'$ have same cache.
	    - if $e' \neq e$, we make $S'$ evict $e'$ and bring $e$ into the cache; now $S$ and $S'$ have the same cache.
	    - We let $S'$ behave exactly like $S$ for remaining requests.
	    - $S'$ is no longer reduced, but can be transformed into a reduced schedule that agrees with FF through first $j+1$ steps.
	- Case 3c: $g \neq e, f$. 
		- $S$ evicts $e$ otherwise $S'$ could have taken the same action.
	    - make $S'$ evict $f$.
	    - now $S$ and $S'$ have the same cache.
	    - let $S'$ behave exactly like $S$ for the remaining requests.
  
This proof shows that S_FF is optimal. Now that we have that, optimality implies that any other algorithm produces either the same number or more misses, so the number of misses is either equal to, or more than S_FF. Therefore, the number of misses OPTFF produces is no larger than that of any arbitrary algorithm ( A ).