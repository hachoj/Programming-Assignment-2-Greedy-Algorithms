Question 2: Bad Sequence for LRU or FIFO

Yes, a sequence like this exists. For cache size k=3, one example request sequence is 1,2,3,4,1,2,5,1,2,3,4,5.
For this sequence OPTFF incurs 7 misses while LRU incurs 10 misses, and the reason for this is that OPTFF knows
the future request sequence and always evicts the item whose next use is farthest in the future. This means that
it avoids evicting values that will be needed again soon. On the other hand, LRU only uses past information and evicts
the least recently used item even if that item is about to be requested again. In this sequence, that causes LRU to
make worse eviction choices and leads to more misses. As a result, this example shows that for k=3 there does exist a
sequence where OPTFF has fewer misses than LRU. 
